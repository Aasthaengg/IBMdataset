n, k, *h = map(int, open(0).read().split())
h += [0] * 200
dp = [0] + [float("inf")] * 100200
for i in range(1, n):
  dp[i] = min(dp[i-a] + abs(h[i] - h[i-a]) for a in range(1, k + 1))
print(dp[n - 1])