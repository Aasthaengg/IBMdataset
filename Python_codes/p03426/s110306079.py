import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy,bisect
#from operator import itemgetter
#from heapq import heappush, heappop
#import numpy as np
#from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
#from scipy.sparse import csr_matrix

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
nf = lambda: float(ns())
na = lambda: list(map(int, stdin.readline().split()))
nb = lambda: list(map(float, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

H, W, D =na()
A = [na() for _ in range(H)]
Q = ni()
d = {}
for i in range(H):
    for j in range(W):
        d[A[i][j]] = (i, j)

dp = [0 for _ in range(H*W+1)]

for i in range(1, D+1):
    dp[i] = 0

for i in range(D+1, H*W+1):
    ni, nj = d[i]
    pi, pj = d[i - D]
    dp[i] = dp[i - D] + abs(ni - pi) + abs(nj - pj)

for i in range(Q):
    ans = 0
    l, r = na()
    ans = dp[r] - dp[l]
    print(ans)