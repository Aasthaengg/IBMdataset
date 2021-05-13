n=int(input())
h=list(map(int,input().split()))
l=-1
r=-1
i=0
ans=0
while sum(h)!=0:
	if l==-1 and h[i]!=0:
		l=i
	if l!=-1 and h[i]==0:
		r=i-1
	elif r==-1 and i==n-1:
		r=i
	if l!=-1 and r!=-1:
		tmp=min(h[l:r+1])
		ans+=tmp
		for j in range(l,r+1):
			h[j]-=tmp
		l=-1
		r=-1
		i=-1
	i+=1
print(ans)