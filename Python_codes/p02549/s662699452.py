N, K = map(int, input().split())
L, R = [], []
for _ in range(K):
    tmpl, tmpr = map(int, input().split())
    L.append(tmpl)
    R.append(tmpr)
MOD = 998244353

dp = [0] * (N + 1)
dp[1] = 1
dp[2] = -1
for i in range(1, N + 1):
    dp[i] = dp[i - 1] + dp[i]
    for l, r in zip(L, R):
        if i + l < N + 1:
            dp[i + l] += dp[i]
            dp[i + l] %= MOD
        if i + r + 1 < N + 1:
            dp[i + r + 1] -= dp[i]
            dp[i + r + 1] %= MOD
print(dp[N] % MOD)
