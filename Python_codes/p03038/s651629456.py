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
aa = Counter(LIST())
aa = sorted(aa.items(), key=itemgetter(0))
a = [[aa[i][1], aa[i][0]] for i in range(len(aa))]
b = sorted([LIST() for i in range(m)], key=itemgetter(1), reverse=True)

ans = 0
i = j = 0
while i < len(b) and j < len(a) and b[i][1] > a[j][1]:
    if b[i][0] >= a[j][0]:
        ans += b[i][1]*a[j][0]
        b[i][0] -= a[j][0]
        a[j][0] = 0
        j += 1
    else:
        ans += b[i][1]*b[i][0]
        a[j][0] -= b[i][0]
        b[i][0] = 0
        i += 1
reg = j
if reg < len(a):
    for i in range(j, len(a)):
        ans += a[i][0]*a[i][1]
print(ans)