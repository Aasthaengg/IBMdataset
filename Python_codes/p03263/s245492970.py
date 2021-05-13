import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy,bisect
from operator import itemgetter
#from heapq import heappush, heappop
#import numpy as np
#from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
#from scipy.sparse import csr_matrix
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
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
a = [na() for _ in range(H)]
N = 0
ans = []
for y in range(H):
    for x in range(W):
        #print(y, x, a[y][x])
        if a[y][x] % 2 == 0:
            continue
        else:
            nx = x + 1
            ny = y + 1
            if 0 <= nx < W and a[y][nx] % 2 == 1:
                N += 1
                a[y][nx] += 1
                a[y][x] -=1
                ans.append((y+1, x+1, y+1, nx+1))
            elif 0 <= ny < H and a[ny][x] % 2 == 1:
                N += 1
                a[ny][x] += 1
                a[y][x] -=1
                ans.append((y+1, x+1, ny+1, x+1))
            elif 0 <= ny < H:
                N += 1
                a[ny][x] += 1
                a[y][x] -=1
                ans.append((y+1, x+1, ny+1, x+1))
            elif 0 <= nx < W:
                N += 1
                a[y][nx] += 1
                a[y][x] -=1
                ans.append((y+1, x+1, y+1, nx+1))
print(N)
for x in ans:
    print(*x)