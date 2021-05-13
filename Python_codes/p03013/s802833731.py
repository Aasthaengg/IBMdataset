n, m = map(int, input().split())
stairs = [i for i in range(1, n+1)]
a = [0 for _ in range(m)]
for i in range(m):
  a[i] = int(input())
a = set(a)
  
dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n+1):
  if i in a:
    continue
  dp[i] = dp[i-1]
  if i > 1:
    dp[i] += dp[i-2]

print(dp[n] % 1000000007)