def main():
	X,Y,Z,k=map(int,input().split())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	c=list(map(int,input().split()))
	ab=[]
	for x in a:
		for y in b:
			ab.append(x+y)
	ab.sort(reverse=True)
	if len(ab)>k:
		ab=ab[:k+1]
	c.sort()
	l=0
	r=max(ab)+max(c)+1
	import bisect
	while r-l>1:
		cnt=0
		mid=(l+r)//2
		for x in ab:
			cnt+=Z-bisect.bisect_left(c,mid-x)
		if cnt>=k:
			l=mid
		else:
			r=mid
	ans=[]
	for i in range(len(ab)):
		for j in range(bisect.bisect_left(c,l-ab[i]),Z):
			ans.append(ab[i]+c[j])
	ans.sort(reverse=True)
	for i in range(min(k,len(ans))):
		print(ans[i])
if __name__=="__main__":
	main()