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

def dfs(y0, y1, x0, x1):
    global k
    m = 0
    tmp = []
    for i in range(y0, y1):
        for j in range(x0, x1):
            a[i][j] = k
            if s[i][j] == '#':
                tmp.append([i, j])
                m += 1
            if m == 2:
                break
        else:
            continue
        break
    if m == 1:
        k -= 1
    else:
        if tmp[0][0] != tmp[1][0]:
            pos = max(tmp[0][0], tmp[1][0])
            dfs(y0, pos, x0, x1)
            dfs(pos, y1, x0, x1)
        else:
            pos = max(tmp[0][1], tmp[1][1])
            dfs(y0, y1, x0, pos)
            dfs(y0, y1, pos, x1)

h, w ,k = MAP()
s = []
a = [[0]*w for i in range(h)]
for i in range(h):
    s.append(input())

dfs(0, h, 0, w)
for i in range(h):
    print(*a[i][:])