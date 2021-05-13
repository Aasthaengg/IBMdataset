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
    ans = [0]*n
    dist = [-1]*n
    que = deque([0])
    dist[0] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in g[v]:
            if dist[w] > -1:
                continue
            dist[w] = d + 1
            ans[w] = v + 1
            que.append(w)
    return ans[1:]

n, m = MAP()
g = [[] for i in range(n)]
for i in range(m):
    A, B =MAP()
    g[A-1].append(B-1)
    g[B-1].append(A-1)

print("Yes")
for x in bfs():
    print(x)