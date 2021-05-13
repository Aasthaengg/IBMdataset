from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
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

h, w = MAP()
s = []
for i in range(h):
    s.append(input())
a = [[0]*w for i in range(h)]
b = [[0]*w for i in range(h)]

for i in range(h):
    tmp = 0
    for j in range(w):
        if s[i][j] == '.':
            tmp += 1
            a[i][j] = tmp
        else:
            tmp = 0
    tmp = 0
    for j in range(w-1, -1, -1):
        if s[i][j] == '.':
            tmp = max(tmp, a[i][j])
            a[i][j] = tmp
        else:
            tmp = 0

ans = 0
for j in range(w):
    tmp = 0
    for i in range(h):
        if s[i][j] == '.':
            tmp += 1
            b[i][j] = tmp
        else:
            tmp = 0
    tmp = 0
    for i in range(h-1, -1, -1):
        if s[i][j] == '.':
            tmp = max(tmp, b[i][j])
            b[i][j] = tmp
        else:
            tmp = 0
        ans = max(ans, a[i][j]+b[i][j]-1)
print(ans)