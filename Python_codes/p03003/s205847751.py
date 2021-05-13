N, M = map(int, input().split())
S = tuple(map(int, input().split()))
T = tuple(map(int, input().split()))
MOD = 10 ** 9 + 7

dp = [[1] * (M + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(M):
        dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j]
        if S[i] != T[j]:
            dp[i + 1][j + 1] -= dp[i][j]
        dp[i + 1][j + 1] %= MOD
print(dp[N][M])
