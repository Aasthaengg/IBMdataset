n,k=map(int,input().split())
l=0
r=10**9+1
ww=[]
for i in range(n):
	ww.append(int(input()))
while l<r:
	mid=(r+l)//2
	cnt=0
	tr=1
	for i in range(n):
		w=ww[i]
		if w>mid or tr>k:
			tr=10**18
			l=mid+1
			break
		if w+cnt<=mid:
			cnt+=w
		else:
			cnt=w
			tr+=1
	if tr<=k:
		r=mid
	else:
		l=mid+1
print(l)

	

