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

n = INT()
a = [inf]*100001

a[0] = 0
for i in range(1,100001):
    a[i] = min(a[i], a[i-1]+1)
    j = 1
    while i - 6**j >= 0:
        a[i] = min(a[i], a[i-6**j]+1)
        j += 1
    j = 1
    while i - 9**j >= 0:
        a[i] = min(a[i], a[i-9**j]+1)
        j += 1

print(a[n])