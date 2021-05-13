from math import ceil,floor,comb,factorial,gcd,pow,sqrt,log2,cos,sin,tan,pi,inf
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

n = INT()
a = LIST()

ans = 1
flag = 0
inv = 0
for i in range(1, n):
    if inv == 0:
        if a[i] - a[i-1] > 0:
            if flag == -1:
                inv = 1
            flag = 1
        elif a[i] - a[i-1] < 0:
            if flag == 1:
                inv = 1
            flag = -1
    else:
        if a[i] - a[i-1] > 0:
            ans += 1
            flag = 1
            inv = 0
        elif a[i] - a[i-1] < 0:
            ans += 1
            flag = -1
            inv = 0

if inv == 1:
    ans += 1
    
print(ans)