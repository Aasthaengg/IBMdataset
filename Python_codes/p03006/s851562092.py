from collections import defaultdict
n = int(input())
balls = []
diffs = [[None] * n for _ in range(n)]
for _ in range(n):
    x, y = [int(i) - 1 for i in input().split()]
    balls.append((x, y))

d = defaultdict(int)

# 各ボールの差分を計算する
for i in range(n):
    for j in range(n):
        ax, ay = balls[i]
        bx, by = balls[j]
        diffs[i][j] = (bx - ax, by - ay)
        if bx - ax != 0 or by - ay != 0:  # p≠0 または q≠0
            d[(bx - ax, by - ay)] += 1

_max = 0

for k, v in d.items():
    _max = max(_max, v)

print(n - _max)
