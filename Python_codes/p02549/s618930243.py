N, K = map(int, input().split())
S = []
for _ in range(K):
    S.append(list(map(int, input().split())))
mod = 998244353

dp = [0 for _ in range(2 * N + 1)]
dp[1] = 1

cum = [0 for _ in range(2 * N + 1)]
cum[1] = 1

for i in range(N):
    for l, r in S:
        dp[i + 1] += cum[i - l + 1] - cum[i - r]
        dp[i + 1] %= mod
    cum[i + 1] = cum[i] + dp[i + 1]
    cum[i + 1] %= mod
print(dp[N])
