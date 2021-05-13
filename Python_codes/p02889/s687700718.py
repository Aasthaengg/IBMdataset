import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
from bisect import *
from collections import *
from heapq import *
import functools
import itertools
import math
INF = float('inf')
MOD = 10**9+7

def dijkstra(s, edges):
    dist = [INF] * len(edges)
    dist[s], h = 0, []
    heappush(h, (0, s))
    while (len(h)):
        dv, v = heappop(h)
        if dv > dist[v]:
            continue
        for u, cost in edges[v]:
            if dv + cost < dist[u]:
                dist[u] = dv + cost
                heappush(h, (dist[u], u))
    return dist

N, M, L = map(int, input().split())
es = [[INF] * N for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    es[a][b] = es[b][a] = c
for i in range(N):
    es[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            tmp = es[i][k] + es[k][j]
            if tmp < es[i][j]:
                es[i][j] = tmp
es2 = [[] for i in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        if es[i][j] <= L:
            es2[i].append((j, 1))
            es2[j].append((i, 1))
dist = [dijkstra(i, es2) for i in range(N)]
Q = int(input())
for i in range(Q):
    s, t = map(lambda x: int(x)-1, input().split())
    ans = dist[s][t]
    if ans == INF:
        ans = 0
    print(ans-1)
