n = int(input())
dp = [0] * (10**6+5)
for i in range(1, n+1):
  dp[i] = float("inf")
  power = 1
  while True:
    if i - power < 0:
      break
    dp[i] = min(dp[i], dp[i-power] + 1)
    power *= 6
  power = 1
  while True:
    if i - power < 0:
      break
    dp[i] = min(dp[i], dp[i-power] + 1)
    power *= 9
print(dp[n])
