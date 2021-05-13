# https://atcoder.jp/contests/abc079/tasks/abc079_d

from collections import defaultdict

H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
for w in range(10):
    for u in range(10):
        for v in range(10):
            if c[u][v] > c[u][w] + c[w][v]:
                c[u][v] = c[u][w] + c[w][v]

cost = 0
for _ in range(H):
    lv = map(int, input().split())
    for v in lv:
        if v >= 0:
            cost += c[v][1]
print(cost)
