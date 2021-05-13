N, M = map(int, input().split())
C = list(map(int, input().split()))
C.sort()

dp = [[10**18]*(N+10) for _ in range(M+10)]
dp[0][0] = 0

for i in range(M):
    for j in range(N+1):
        if j - C[i] >= 0:
            dp[i+1][j] = min(dp[i][j - C[i]] + 1, dp[i][j], dp[i+1][j - C[i]] + 1)
        else:
            dp[i+1][j] = dp[i][j]



print(dp[M][N])
