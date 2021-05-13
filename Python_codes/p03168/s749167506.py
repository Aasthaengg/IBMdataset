N=int(input())
p=list(map(float,input().split()))

dp=[[0]*(N+1) for i in range(N+1)]
dp[0][0]=1
for i in range(N):
    for j in range(N+1):
        if j==0:
            dp[i+1][j]=dp[i][j]*(1-p[i])
        else:
            dp[i+1][j]=dp[i][j]*(1-p[i])+dp[i][j-1]*p[i]
print(sum(dp[N][N//2+1:]))