pos=[0]*(200005)
ind=0
for i in range(int(input())):
	x=int(input())
	if x!=pos[ind]:
		ind+=1
		pos[ind]=x
ans=[0]*(ind+1)
per=[0]*200005
ans[0]=1
for i in range(1,ind+1):
	per[pos[i]]=(per[pos[i]]+ans[i-1])%1000000007
	ans[i]=per[pos[i]]
print(ans[i])