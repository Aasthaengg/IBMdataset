from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
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

h, n = MAP()
a = [0]*n
b = [0]*n
dp = [inf]*(h+1)
dp[0] = 0
# dp[j]: ダメージ>=jとするために必要な魔力の最小値

for i in range(n):
    a[i], b[i] = MAP()

for i in range(n):
    for j in range(0,h+1):
        if j < a[i]:
            dp[j] = min(dp[j], b[i])
        else:
            dp[j] = min(dp[j], dp[j-a[i]]+b[i])

print(dp[h])