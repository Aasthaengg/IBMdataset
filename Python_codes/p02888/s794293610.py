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
l = sorted(LIST())

ans = 0
for i in range(n-2):
    right = i + 2
    for j in range(i+1, n-1):
        left = j + 1
        while right < n-1 and l[right] < l[i] + l[j]:
            right += 1
        ans += right - left
        if l[right] < l[i] + l[j]:
            ans += 1
print(ans)