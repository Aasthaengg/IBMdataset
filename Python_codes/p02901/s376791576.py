n, m = map(int, input().split())
price = [0] * m
treasure = [0] * m
for i in range(m):
  price[i], _ = map(int, input().split())
  for c in map(int, input().split()):
    treasure[i] += 1 << c-1
dp = [10 ** 8 + 1] * (1 << n)
dp[0] = 0
for bit in range((1 << n) - 1):
  cost = dp[bit]
  for i in range(m):
    next_bit = treasure[i] | bit
    next_cost = price[i] + cost
    dp[next_bit] = min(dp[next_bit], next_cost)
if dp[-1] > 10 ** 8:
  print(-1)
else:
  print(dp[-1])