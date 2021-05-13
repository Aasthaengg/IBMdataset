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

n = ni()
a = na()
a.sort(reverse=True)
ans = -1
t = a[0]
target = (a[0] + (2 - 1)) // 2
#print(target)
pre = inf
if n == 2:
    print(max(a), min(a))
    sys.exit()
for i in range(1, n):
    #print(pre)
    dif = abs(target - a[i])
    if pre < dif:
        print(t, a[i-1])
        sys.exit()
    else:
        pre = dif
