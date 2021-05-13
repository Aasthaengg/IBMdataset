import copy
from itertools import product, combinations

N = int(input())

dp = []
for _ in range(N):
    dp.append(list(map(int, input().split(' '))))

original = copy.deepcopy(dp)

for k, i, j in product(range(N), repeat=3):
    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

if dp == original:
    cost = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(N):
                if k == i or k == j:
                    continue
                if dp[i][j] == dp[i][k] + dp[k][j]:
                    break
            else:
                cost += dp[i][j]
    print(cost)
else:
    print(-1)
