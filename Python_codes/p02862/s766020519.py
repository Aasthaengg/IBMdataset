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

def mycmb(n,r,p):
    r = min(r,n-r)
    if r == 0:
        return 1
    over = reduce(lambda x,y:x*y%p,range(n,n-r,-1))
    under = reduce(lambda x,y:x*y%p,range(1,r+1))
    return (over * pow(under,p-2,p))%p

x, y = MAP()
a = 2*x - y
b = 2*y - x

if a >= 0 and b >= 0 and a % 3 == 0 and b % 3 == 0:
    a //= 3
    b //= 3
    ans = mycmb(a+b, a, 10**9+7)
else:
    ans = 0

print(ans)