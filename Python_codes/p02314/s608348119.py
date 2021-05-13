n,m=map(int,input().split())
c=list(map(int,input().split()))

dp=[float('inf')]*(n+1)
dp[0]=0
for i in range(n+1):
    if dp[i]==float('inf'):continue
    for j in c:
        if i+j>n:continue
        dp[i+j]=min(dp[i]+1,dp[i+j])
print(dp[-1])
