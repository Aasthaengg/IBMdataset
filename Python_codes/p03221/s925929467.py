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
p = [[i]+LIST() for i in range(m)]
q = [0]*(n+1)

p.sort(key=itemgetter(2))
for x in p:
    q[x[1]] += 1
    x.append(q[x[1]])

p.sort(key=itemgetter(0))
for x in p:
    print(str(x[1]).zfill(6)+str(x[3]).zfill(6))