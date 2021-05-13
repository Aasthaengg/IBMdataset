from itertools import product
import numpy as np

H, W = map(int, input().split(' '))

INF = 10 ** 9

dp = np.ones(shape=(10, 10), dtype=int) * INF

for i in range(10):
    costs = tuple(map(int, input().split(' ')))
    for j in range(10):
        dp[i][j] = costs[j]

for k, i in product(range(10), repeat=2):
    dp[i] = np.minimum(dp[i], dp[i][k] + dp[k])

cost = 0
for _ in range(H):
    numbers = tuple(map(int, input().split(' ')))
    for n in numbers:
        if n < 0:
            continue
        cost += dp[n][1]

print(cost)
