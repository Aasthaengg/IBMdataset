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

h, w = MAP()
s = [input() for i in range(h)]
dp = [[inf]*w for i in range(h)]

if s[0][0] == '#':
    dp[0][0] = 1
else:
    dp[0][0] = 0

for i in range(h):
    for j in range(w):
        if i+1 < h:
            if s[i][j] == '.' and s[i+1][j] == '#':
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            else:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        if j+1 < w:
            if s[i][j] == '.' and s[i][j+1] == '#':
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            else:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j])

print(dp[h-1][w-1])