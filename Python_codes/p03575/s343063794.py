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
    que = deque([0])
    c[0] = 1
    while que:
        v = que.popleft()
        for w in g[v]:
            if c[w] == 1:
                continue
            c[w] = 1
            que.append(w)

n, m  = MAP()
g = [[] for i in range(n)]
a = [0]*m
b = [0]*m
for i in range(m):
    a[i], b[i] = MAP()
    a[i] -= 1
    b[i] -= 1
    g[a[i]].append(b[i])
    g[b[i]].append(a[i])

ans = 0
for i in range(m):
    g[a[i]].remove(b[i])
    g[b[i]].remove(a[i])
    c = [0]*n
    bfs()
    for j in range(n):
        if c[j] == 0:
            ans += 1
            break
    g[a[i]].append(b[i])
    g[b[i]].append(a[i])

print(ans)