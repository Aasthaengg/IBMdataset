N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
MOD = 10 ** 9 + 7

dp = [[0] * (M + 1) for i in range(N + 1)]
dp_sum = [[0] * (M + 1) for i in range(N + 1)]

dp[0][0] = 1
for i, s in enumerate(S, start=1):
    for j, t in enumerate(T, start=1):
        if s == t:
            dp[i][j] = dp_sum[i - 1][j - 1] + 1
            dp[i][j] %= MOD
        dp_sum[i][j] = dp_sum[i - 1][j] + dp_sum[i][j - 1] - dp_sum[i - 1][j - 1] + dp[i][j]
        dp_sum[i][j] %= MOD

ans = 0
for i in range(N + 1):
    for j in range(M + 1):
        ans += dp[i][j]
        ans %= MOD

print(ans % MOD)
