from sys import stdin
def input():
    return stdin.readline().strip()

n, ma, mb = map(int, input().split())
a, b, c = [], [], []
for _ in range(n):
    i, j, k = map(int, input().split())
    a.append(i)
    b.append(j)
    c.append(k)

sum_a = sum(a) + 1
sum_b = sum(b) + 1

# dpを商品を増やすごとに更新する
dp = [[float('inf')] * sum_b for _ in range(sum_a)]
dp[0][0] = 0

from copy import deepcopy
for i in range(n):
    new_dp = deepcopy(dp)
    ai, bi, ci = a[i], b[i], c[i]
    for x in range(sum_a - ai):
        for y in range(sum_b - bi):
            new_dp[x+ai][y+bi] = dp[x][y] + ci
    for x in range(sum_a):
        for y in range(sum_b):
            if dp[x][y] > new_dp[x][y]:
                dp[x][y] = new_dp[x][y]

ans = float('inf')
for x in range(1, sum_a):
    for y in range(1, sum_b):
        if x * mb == y * ma and dp[x][y] < ans:
            ans = dp[x][y]

if ans == float('inf'):
    print(-1)
else:
    print(ans)