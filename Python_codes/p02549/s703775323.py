mod = 998244353
n, k = map(int, input().split())
left = []
right = []
for _ in range(k):
  l, r = map(int, input().split())
  left.append(l)
  right.append(r)
dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n+1):
  for j in range(k):
    dp[i] += dp[max(0, i - left[j])] - dp[max(0, i - right[j] - 1)]
    dp[i] %= mod
  dp[i] = (dp[i-1] + dp[i]) % mod
print((dp[n] - dp[n-1]) % mod)