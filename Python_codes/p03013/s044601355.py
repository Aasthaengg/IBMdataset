n, m = map(int, input().split())
A = [True] * (n+1)
for _ in range(m):
  a = int(input())
  A[a] = False

mod = 10**9 + 7
dp = [0] * (n+1)
dp[0] = 1
if A[1]:
  dp[1] = 1

for i in range(2, n+1):
  if A[i]:
    dp[i] = dp[i-1] + dp[i-2]
    dp[i] %= mod

print(dp[n])