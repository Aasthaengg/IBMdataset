# -*- coding: utf-8 -*-
import numpy as np
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect


def zz():
    return list(map(int, input().split()))


def z():
    return int(input())


def S():
    return input()


def C(line):
    return [input() for _ in range(line)]

from heapq import heapify, heappush, heappop
def dijkstra(path, N, start):
    visited = [False] * N
    que = [(0, start)]
    heapify(que)  # 始点aから各頂点への(距離, 頂点ID)
    dist = [-1] * N  # 始点aから各頂点への距離
    dist[start] = 0  # 始点aからaへの距離は0
    while que:
        d, v = heappop(que)  # 始点から最短距離の頂点を(確定ノード)を取り出す
        visited[v] = True  # 確定フラグを立てる
        # 接続先ノードの情報を更新する
        for d, to in path[v]:
            cost = dist[v] + d
            if dist[to] < 0 or cost < dist[to]:
                dist[to] = cost
                if not visited[to]:
                    heappush(que, (cost, to))
    return dist
N = z()
# 0 を頂点とする根付き木を考える
path = [[] for _ in range(N)]
for i in range(N-1):
    u, v, w = zz()
    path[u-1].append((w, v-1))
    path[v-1].append((w, u-1))
dist = dijkstra(path, N, 0)
# print(dist)
ans = [0] * N
for i, d in enumerate(dist):
    if (d % 2 == 0):
        ans[i] = 0 
    else:
        ans[i] = 1

print(*ans, sep='\n')
            
