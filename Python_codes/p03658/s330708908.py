n,k=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
ans=int(0)
for i in range(n-k,n):
	ans+=A[i]
print(ans)