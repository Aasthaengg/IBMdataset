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

n = INT()
s = [input() for i in range(n)]

a = 0
b = 0
ab = 0
c = 0
for x in s:
    ab += x.count("AB")
    if x[0] == 'B' and x[-1] == 'A':
        c += 1
    elif x[0] == 'B':
        b += 1
    elif x[-1] == 'A':
        a += 1
    
print( ab + max(c-1, 0) + min(a, b) + (1 if a + b != 0 and c > 0 else 0))