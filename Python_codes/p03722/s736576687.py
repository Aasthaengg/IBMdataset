import sys
from collections import Counter, deque, defaultdict
from math import factorial
import heapq, bisect
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**15 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

n,m = MAP()
E = [[(0,0,0)]for i in range(m)]
for i in range(m):
    a,b,cost = MAP()
    E[i] = (a-1, b-1, -1*cost)

d = [INF]*n
d[0] = 0
for i in range(n-1):
    for e in E:
        if d[e[0]] != INF and d[e[0]]+e[2] < d[e[1]]:
            d[e[1]] = d[e[0]]+e[2]
res =  d[n-1]

for e in E:
    if d[e[0]] != INF and d[e[0]]+e[2] < d[e[1]]:
            d[e[1]] = d[e[0]]+e[2]




if  res != d[n-1]:
    print('inf')
else:
    print(res*-1)
