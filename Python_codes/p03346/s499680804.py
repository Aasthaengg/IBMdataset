N, *P = map(int, open(0).read().split())
dp = [0] * (N + 1)
for p in P:
    dp[p] = dp[p - 1] + 1
print(N - max(dp))
