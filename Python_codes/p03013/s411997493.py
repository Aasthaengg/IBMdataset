n, m = map(int, input().split())
a = set()
for _ in range(m):
  a_ = int(input())
  a.add(a_)

dp = [0] * (n+1)
if 1 not in a:
  dp[1] = 1
if 2 not in a and n != 1:
  dp[2] = dp[1] + 1
for i in range(3, n+1):
  if i not in a:
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%(10**9+7))