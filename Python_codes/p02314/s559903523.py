from itertools import product

value, variety = map(int, input().split())
coins = list(map(int, input().split()))
dp = [float("inf") for _ in range(value + 1)]
dp[0] = 0
for (c,j) in product(coins,list(range(value + 1))):
    if c <= j:
        dp[j] = min(dp[j], dp[j - c] + 1)
    else:
        dp[j] = dp[j]
print(dp[value])