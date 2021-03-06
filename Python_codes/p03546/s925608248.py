import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy,bisect
from operator import itemgetter
from heapq import heappush, heappop
import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
nf = lambda: float(ns())
na = lambda: list(map(int, stdin.readline().split()))
nb = lambda: list(map(float, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces


H, W = na()
c = [na() for _ in range(10)]
A = [na() for _ in range(H)]
adj = [[] for _ in range(10)]



# cost[i][j]: 頂点v_iから頂点v_jへ到達するための辺コストの和
for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])
ans = 0
for y in range(H):
    for x in range(W):
        if A[y][x] != -1:
            #print(ans)
            ans += c[A[y][x]][1]
print(ans)

