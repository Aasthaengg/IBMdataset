n, *h = map(int, open(0).read().split())
dp = [0] + [float("inf")] * -~n
for i in range(1, n):
  dp[i] = min(dp[i-a] + abs(h[i] - h[i-a]) for a in [1,2])
print(dp[n - 1])