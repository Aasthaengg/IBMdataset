n,ma,mb=map(int,input().split())
dp=[[[10**4 for _ in range(401)] for __ in range(401)] for ___ in range(n+1)]
for i in range(n+1):
    dp[i][0][0]=0
for i in range(n):
    a,b,c=map(int,input().split())
    for j in range(401):
        for k in range(401):
            if j>=a and k>=b:
            	dp[i+1][j][k]=min(dp[i][j][k],dp[i][j-a][k-b]+c)
            else:
                dp[i+1][j][k]=dp[i][j][k]
ans=float("INF")
for j in range(1,401):
    for k in range(1,401):
        if ma*k==mb*j:
            ans=min(ans,dp[n][j][k])
if ans==10**4:
    print(-1)
else:
    print(ans)