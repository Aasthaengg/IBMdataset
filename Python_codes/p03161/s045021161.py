n, k, *h = map(int, open(0).read().split())
dp = [0] * n
for i in range(1, n):
  dp[i] = min(dp[i-a] + abs(h[i] - h[i-a]) for a in range(1, min(i, k) + 1))
print(dp[n - 1])