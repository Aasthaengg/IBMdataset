n = int(input())
dp = [10*9]*100001
dp[0] = 0
for i in range(1, n+1):
  c6 = 0
  c9 = 0
  while 6 ** c6 <= i:
    c6 += 1
  while 9 ** c9 <= i:
    c9 += 1
  dp[i] = min(dp[i-1]+1, dp[i-6**(c6-1)]+1, dp[i-9**(c9-1)]+1)

print(dp[n])