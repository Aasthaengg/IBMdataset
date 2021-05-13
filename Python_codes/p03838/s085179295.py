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

x, y = MAP()

if 0 <= x < y:
    ans = y - x
elif 0 <= y < x:
    ans = min(y+x+1, -y+x+2)
elif x <= 0 <= y:
    if abs(x) <= abs(y):
        ans = min(y-x, y+x+1)
    else:
        ans = min(y-x, -y-x+1)
elif y <= 0 <= x:
    if abs(x) <= abs(y):
        ans = - y - x + 1
    else:
        ans = y + x + 1
elif x < y <= 0:
    ans = y - x
elif y < x <= 0:
    ans = min(-y-x+1, -y+x+2)

print(ans)