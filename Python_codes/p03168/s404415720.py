N=int(input())
p=list(map(float,input().split()))

dp=[[0]*(N+1) for _ in range(N+1)]

dp[0][0]=1

for i in range(1,N+1):
    dp[i][0]=dp[i-1][0]*(1-p[i-1])

for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = dp[i-1][j]*(1-p[i-1]) + dp[i-1][j-1]*p[i-1]

print(sum(dp[N][(N//2+1):]))