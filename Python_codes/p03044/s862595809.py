import sys
import itertools
# import numpy as np
import time
import math

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())

adj = [[] for i in range(n)]
for i in range(n - 1):
    u, v, w = map(int, readline().split())
    u -= 1
    v -= 1
    adj[u].append((w, v))
    adj[v].append((w, u))
# print(adj)

visited = [False for _ in range(n)]
dist = [0 for _ in range(n)]
def dfs(x, depth):
    if visited[x]:
        return
    visited[x] = True
    dist[x] = depth
    for y in adj[x]:
        dfs(y[1], depth + y[0])

dfs(0, 0)

# print(dist)
for d in dist:
    if d % 2 == 0:
        print(0)
    else:
        print(1)