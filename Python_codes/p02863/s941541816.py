n,t=list(map(int,input().split()))
ab=sorted([list(map(int,input().split())) for _ in range(n)],key=lambda x:x[0])

dp=[[-10**10]*(t+1) for _ in range(n+1)]
dp[0][0]=0
dp[1][0]=0
ans=ab[0][1]
for i in range(1,n):
    for j in range(t):
        dp[i+1][j]=max(dp[i][j],dp[i][j-ab[i-1][0]]+ab[i-1][1] if j>=ab[i-1][0] else -10**10)
        ans=max(ans,dp[i+1][j]+ab[i][1])

print(ans)