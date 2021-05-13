from math import ceil,floor,comb,factorial,gcd,pow,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heappop,heappush
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n, m = MAP()
a = LIST()
b = [LIST() for i in range(m)]
b.sort(key=itemgetter(1), reverse=True)

c = []
for i in range(m):
    c += [b[i][1]]*b[i][0]
    if len(c) > n:
        break

a += c
a.sort(reverse=True)
print(sum(a[:n]))