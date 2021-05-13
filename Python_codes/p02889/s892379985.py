# -*- coding: utf-8 -*-
# E

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

import sys
input = sys.stdin.readline

INF = float("INF")

N, M, L = map(int, input().split())

cost = [[INF] * N for _ in range(N)]
for i in range(N):
    cost[i][i] = 0

for _ in range(M):
    v1, v2, w = map(int, input().split())
    v1, v2 = v1-1, v2-1
    cost[v1][v2] = w
    cost[v2][v1] = w

for k in range(N):
    for i in range(N):
        for j in range(N):
            if cost[i][j] > cost[i][k] + cost[k][j]:
                cost[i][j] = cost[i][k] + cost[k][j]

for i in range(N):
    for j in range(N):
        if cost[i][j] == 0:
            continue
        elif cost[i][j] <= L:
            cost[i][j] = 1
        else:
            cost[i][j] = INF

for k in range(N):
    for i in range(N):
        for j in range(N):
            if cost[i][j] > cost[i][k] + cost[k][j]:
                cost[i][j] = cost[i][k] + cost[k][j]

q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    if cost[s-1][t-1] == INF:
        print(-1)
    else:
        print(cost[s-1][t-1] - 1)
