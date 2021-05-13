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

h, w, k = MAP()
s = []
p = []
q = []
for i in range(h):
    s.append(input())
    if s[i].count('#') > 0:
        p.append(i)
    else:
        q.append(i)

a = [[0]*w for i in range(h)]
num = 0
if p:
    for i in p:
        num += 1
        m = 0
        while s[i][m] == '.':
            a[i][m] = num
            m += 1
        if m < w:
            if s[i][m] == '#':
                a[i][m] = num
                m += 1
            if m < w:
                for j in range(m, w):
                    if s[i][j] == '#':
                        num += 1
                    a[i][j] = num

if q:
    for i in q:
        m = i
        while m < h and a[m][0] == 0:
            m += 1
        if m >= h:
            m = i
            while m > 0 and a[m][0] == 0:
                m -= 1
        a[i][:] = a[m][:]
for i in range(h):
    print(*a[i][:])