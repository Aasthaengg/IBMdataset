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

def dijkstra_path(s, edges):
    dist = [INF for i in range(len(edges))]
    dist[s], h, p = 0, [], [-1]*len(edges)
    heappush(h, (0, s))
    while (len(h)):
        dv, v = heappop(h)
        if dv > dist[v]:
            continue
        for u, cost in edges[v]:
            tmp = dv+cost
            if tmp < dist[u]:
                dist[u] = tmp
                p[u] = v
                heappush(h, (tmp, u))
    return dist, p

N, M = map(int, input().split())
S = input()
ids = []
for i, x in enumerate(S):
    if x == '0':
        ids.append(-i)
ids = ids[::-1]
l = len(ids)
es = [[] for i in range(N+1)]
for i in range(N, 0, -1):
    es[i].append((-ids[min(l-1, bisect_right(ids, -i+M)-1)], 1))
d, p = dijkstra_path(N, es)
if d[0] == INF:
    print(-1)
    exit()
vs = []
v = 0
while v != -1:
    vs.append(v)
    v = p[v]
ans = [vs[i+1]-vs[i] for i in range(len(vs)-1)]
print(*ans, sep = ' ')
