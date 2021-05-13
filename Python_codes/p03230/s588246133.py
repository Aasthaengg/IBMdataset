import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce, lru_cache
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = 10**6#float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
#from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N = INT()

lim = int(-(-sqrt(2*N)//1))+1
for i in range(lim):
	if i*(i+1) == 2*N:
		break
else:
	print("No")
	exit()

n = i+1
print("Yes")
print(n)
ans = [[] for _ in range(n)]
cnt = 1
for j in range(n):
	k = j+1
	while k < n:
		ans[j].append(cnt)
		ans[k].append(cnt)
		cnt += 1
		k += 1

for l in range(n):
	print(i, *ans[l])
