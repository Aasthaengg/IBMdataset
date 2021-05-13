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

n = INT()
s = input()

r = s.count('R')
g = s.count('G')
b = n - r - g
ans = r * g * b
for i in range(n):
    d = 1
    j = i + d
    k = j + d
    while k < n:
        if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
            ans -= 1
        d += 1
        j += 1
        k += 2
print(ans)