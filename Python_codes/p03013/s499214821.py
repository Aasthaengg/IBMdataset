n, m = map(int, input().split())
a = [int(input()) for i in range(m)]
l = [1] * (n+1)
for j in a:
  l[j] = 0
x = 10 ** 9 + 7
if m > n // 2:
  print(0)
else:
  dp = [0] * (n+1)
  dp[0] = 1
  if 1 not in a:
    dp[1] = 1
  for i in range(2, n+1):
    if l[i]:
      dp[i] = (dp[i-1] + dp[i-2]) % x
  print(dp[-1])