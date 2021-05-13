N, M = map(int, input().split(' '))
coins = tuple(map(int, input().split(' ')))

dp = [N + 1] * (N + 1)
dp[0] = 0

for i in range(N + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[N])

