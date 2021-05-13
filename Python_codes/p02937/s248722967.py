import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

s = input()
t = input()

if not set(s) >= set(t):
	print(-1)
	exit()

dic = defaultdict(list)
for i, char in enumerate(s, 1):
	dic[char].append(i)

loop = 0
index = -1
for i in range(len(t)):
	idx = bisect(dic[t[i]], index)
	if idx < len(dic[t[i]]):
		index = dic[t[i]][idx]
	else:
		idx = dic[t[i]][0]
		index = idx
		loop += 1

print(len(s)*loop+index)
