INFTY = 10**8
H,N = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
dp = [[INFTY for j in range(H+1)] for i in range(N+1)]
for i in range(N+1):
    dp[i][0]=0
for i in range(1,N+1):
    for j in range(1,H+1):
        dp[i][j] = dp[i-1][j]
        if j<=A[i-1][0]:
            dp[i][j] = min(dp[i][j],A[i-1][1])
        else:
            dp[i][j] = min(dp[i][j],dp[i][j-A[i-1][0]]+A[i-1][1])
print(dp[N][H])