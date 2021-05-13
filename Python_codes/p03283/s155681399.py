import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy,bisect
from operator import itemgetter
#from heapq import heappush, heappop
#import numpy as np
#from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
#from scipy.sparse import csr_matrix
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
nf = lambda: float(ns())
na = lambda: list(map(int, stdin.readline().split()))
nb = lambda: list(map(float, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N, M, Q = na()
dp = [[0] * (N + 3) for _ in range(N + 3)]
for i in range(M):
    l, r = na()
    dp[1][r] += 1
    dp[l+1][r] -= 1
    dp[l][N+1] -= 1

for i in range(N+1):
    for j in range(N+1):
        dp[i][j+1] += dp[i][j]

for j in range(N+1):
    for i in range(N+1):
        dp[i+1][j] += dp[i][j]

for i in range(Q):
    p, q = na()
    print(dp[p][q])
