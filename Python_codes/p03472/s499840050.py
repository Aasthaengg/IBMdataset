from math import ceil,floor,comb,factorial,gcd,pow,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n, h = MAP()
a = [0]*n
b = [0]*n

for i in range(n):
    a[i], b[i] = MAP()

a.sort(reverse=True)
b.sort(reverse=True)

ans = 0
i = 0
while i < n and b[i] > a[0] and h > 0:
    ans += 1
    h -= b[i]
    i += 1

if h > 0:
    ans += (h+a[0]-1)//a[0]

print(ans)