def soin(n):
	ans=[]
	l=int(n**0.5)+1
	for i in range(2,l+1):
		if n%i==0:
			a=[i,0]
			while n%i==0:
				n//=i
				a[1]+=1
			ans+=[a]
	if n>1:
		ans+=[[n,1]]
	return ans
d={}
n=int(input())
for i in range(2,n+1):
	a=soin(i)
	for j in a:
		if j[0] in d:
			d[j[0]]+=j[1]
		else:
			d[j[0]]=j[1]
k=1
for i in d.values():
	k*=(i+1)
print(k%(10**9+7))