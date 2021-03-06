import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees#, log2
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10**9 + 7
#from decimal import *

N, M = MAP()
PY = [LIST() for _ in range(M)]
PY_ = deepcopy(PY)
PY_.sort(key = lambda x: (x[0],x[1]))

tmp = 0
i = 0
lis = []
dic = {}
for p, y in PY_:
	if p == tmp:
		i += 1
	else: 
		lis.append([])
		tmp = p
		i = 1
	dic[str(p)+"_"+str(y)] = str(p).zfill(6)+str(i).zfill(6)

for p, y in PY:
	print(dic[str(p)+"_"+str(y)])