import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy,bisect
from operator import itemgetter
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

N, C = na()
ans = [0] * ((10 ** 5) * 2 + 10)
for i in range(N):
    s, t, c = na()
    ans[s] += 1
    ans[t+1] -= 1

for i in range(len(ans)-1):
    ans[i+1] += ans[i]
print(min(max(ans), C))

 




