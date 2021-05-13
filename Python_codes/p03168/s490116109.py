from collections import defaultdict
N = int(input())
P = list(map(float, input().split()))

dp = defaultdict(float)
dp[(0, 0)] = 1.0

for p in P:
    newDP = defaultdict(float)
    for (X, Y), val in dp.items():
        # 表が出る
        newDP[(X + 1, Y)] += val * p
        # 裏が出る
        newDP[(X, Y + 1)] += val * (1 - p)
    dp = newDP

ans = 0.0
for x in range(N + 1):
    y = N - x
    if x > y:
        ans += dp[(x, y)]

print(ans)