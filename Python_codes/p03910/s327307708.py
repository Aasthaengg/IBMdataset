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

ans = []

def dfs(m):
    if m == 1:
        ans.append(1)
        return 0
    elif m == 2:
        ans.append(2)
        return 0
    elif m == 3:
        ans.append(2)
        ans.append(1)
        return 0
    elif m == 4:
        ans.append(3)
        ans.append(1)
        return 0
    elif m == 5:
        ans.append(3)
        ans.append(2)
        return 0
    else:
        k = ceil(sqrt(1+8*m))//2
        ans.append(k)
        dfs(m-k)

n = INT()
dfs(n)
for x in ans:
    print(x)