import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy,bisect
#from operator import itemgetter
#from heapq import heappush, heappop
#import numpy as np
#from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
#from scipy.sparse import csr_matrix
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
import sys

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
nf = lambda: float(ns())
na = lambda: list(map(int, stdin.readline().split()))
nb = lambda: list(map(float, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

A, B, H, M = na()
l = 360 / 12 * (H + M / 60)
s = 360 / 60 * M
print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(abs(l - s) * math.pi / 180)))