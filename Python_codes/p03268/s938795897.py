from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n, k = MAP()
a = n//k
if k % 2 == 0:
    b = n//(k//2) - a
else:
    b = 0

ans = a + max(a*(a-1)*3,0) + max(a*(a-1)*(a-2),0)
ans += b + max(b*(b-1)*3,0) + max(b*(b-1)*(b-2),0)
print(ans)