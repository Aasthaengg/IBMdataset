mod = 998244353
inv = pow(2, mod-2, mod)
n, s = map(int, input().split())
a = list(map(int, input().split()))
dp = [0]*(s+1)
dp[0] = pow(2, n, mod)
for i in a:
  for j in range(s, i-1, -1):
    dp[j] = (dp[j] + dp[j-i] * inv) % mod
print(dp[s])
