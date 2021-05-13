N=int(input())
A=list(map(int, input().split()))

ans=1
d={}
for i in range(N+1):
	d[i]=0

d[0]=3

for a in A:
	ans*=d[a]
	d[a]-=1
	d[a+1]+=1
	if ans>=10**9+7:
		ans=ans%(10**9+7)


print(ans)


# 2darray [[0] * 4 for i in range(3)]