from sys import stdin
import collections
import math
import itertools

n,m,r   = [int(x) for x in stdin.readline().rstrip().split()]
r_arr = [int(x) for x in stdin.readline().rstrip().split()]

ways = [[int(c)  for c in stdin.readline().rstrip().split()] for _ in range(m)]
inf = float('inf')
cost = [[inf] * n for _ in range(n)]
for i in range(n):
    cost[i][i] = 0

for way in ways:
    cost[way[0]-1][way[1]-1] = way[2]
    cost[way[1]-1][way[0]-1] = way[2]


# ワーシャルフロイド
for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

# rの訪れ方を全パターン試して、最小の距離のものを答えにする。
tours = []
for perm in itertools.permutations(r_arr):
    d = 0
    for i in range(r-1):
        d += cost[perm[i]-1][perm[i+1]-1]
    tours.append(d)
print(min(tours))