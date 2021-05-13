n = int(input())
if n <= 99:
  print(0)
  exit()
if 100 <= n <= 105:
  print(1)
  exit()
dp = [True] + [False] * n
for i in range(100, n + 1):
  if dp[i - 100] or dp[i - 101] or dp[i - 102] or dp[i - 103] or dp[i - 104] or dp[i - 105]:
    dp[i] = True
print([0, 1][dp[n]])