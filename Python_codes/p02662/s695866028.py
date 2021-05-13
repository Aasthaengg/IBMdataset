N, S, *A = map(int, open(0).read().split())
mod = 998244353

dp = [[0] * (S + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
    for j in range(S + 1):
        dp[i + 1][j] += dp[i][j] * 2
        dp[i + 1][j] %= mod
        if j + A[i] <= S:
            dp[i + 1][j + A[i]] += dp[i][j]
            dp[i + 1][j + A[i]] %= mod

print(dp[-1][-1])
