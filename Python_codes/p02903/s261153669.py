from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf,comb
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

h, w, a, b = MAP()

for i in range(h+1):
    for j in range(w+1):
        if a*i + (w-a)*(h-i) == b*j + (h-b)*(w-j):
            aa = i
            bb = j
            break
    else:
        continue
    break

s = [[0]*w for i in range(h)]
sum = [0]*w

for i in range(h):
    tmp = 0
    for j in range(w):
        if ( i < aa and tmp < a ) or ( i >= aa and tmp < w-a ):
            if ( j < bb and sum[j] < b ) or ( j >= bb and sum[j] < h-b ):
               s[i][j] = 1
               tmp += 1
               sum[j] += 1

for i in range(h):
    print(*s[i][:], sep="")