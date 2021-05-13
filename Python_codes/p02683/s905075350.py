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

n, m, x = MAP()
c = []
a = []
for i in range(n):
    A = LIST()
    c.append(A[0])
    a.append(A[1:])
ans = inf
for y in product([0,1], repeat=n):
    b = [0]*m
    tmp = 0
    for i in range(n):
        if y[i] == 1:
            tmp += c[i]
            for j in range(m):
                b[j] += a[i][j]
            if all(b[k]>=x for k in range(m)):
                ans = min(ans, tmp)
if ans == inf:
    ans = -1
print(ans)