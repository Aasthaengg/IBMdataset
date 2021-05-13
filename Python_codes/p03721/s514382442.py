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

n, k = MAP()
c = defaultdict(int)

for i in range(n):
    a, b = MAP()
    c[a] = c[a] + b

d = sorted(c.items(), key=itemgetter(0))
reg = 0
for x in d:
    reg += x[1]
    if reg >= k:
        print(x[0])
        exit()