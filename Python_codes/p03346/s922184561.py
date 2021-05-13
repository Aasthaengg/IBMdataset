N, *P = map(int, open(0))

dp = [0] * (N + 1)
for i, p in enumerate(P):
    dp[p] = dp[p - 1] + 1

print(N - max(dp))
