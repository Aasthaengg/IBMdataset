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

N = int(input())

adj = [[] for _ in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    u = line[0] - 1
    if line[1] == 0:
        continue
    vs = line[2:]
    for v in vs:
        adj[u].append(v - 1)

d = [-1] * N
f = [-1] * N

def dfs(v, t):
    d[v] = t
    nx = t + 1
    for u in adj[v]:
        if d[u] > -1:
            continue
        nx = dfs(u, nx)
    f[v] = nx
    return f[v] + 1

nx = 1
for i in range(N):
    if d[i] > - 1:
        continue
    nx = dfs(i, nx)

for i in range(N):
    print(i + 1, d[i], f[i])

