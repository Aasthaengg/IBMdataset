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

n, m = MAP()
a = list(map(lambda x:int(x)*(-1), input().split()))

heapify(a)
while m > 0:
    m -= 1
    heappush(a, (-1)*(-heappop(a)//2))
print(-sum(a))