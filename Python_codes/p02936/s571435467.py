from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf,comb
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

def bfs():
    dist = [-1]*(n+1)
    que = deque([1])
    dist[1] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in g[v]:
            if dist[w] > -1:
                continue
            dist[w] = d + 1
            ans[w] += ans[v]
            que.append(w)

n, q  = MAP()
g = [[] for i in range(n+1)]
ans = [0]*(n+1)
for i in range(n-1):
    a, b = MAP()
    g[a].append(b)
    g[b].append(a)
for i in range(q):
    p, x = MAP()
    ans[p] += x
#for i in range(1,n+1):
#    ans[i] += ans[g[i]]
bfs()
for i in range(1, n+1):
    print(ans[i])