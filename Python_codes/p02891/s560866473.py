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


S = input()
K = INT()

l = []
tmp = 1
for i in range(1, len(S)):
	if S[i] == S[i-1]:
		tmp += 1
	else:
		l.append(tmp)
		tmp = 1
l.append(tmp)

if S[0] != S[-1]:
	print(sum([x//2 for x in l])*K)
elif len(l) == 1:
	print(len(S)*K//2)
else:
	M = l[1:-1] + [l[0]+l[-1]]
	print(sum([x//2 for x in M])*(K-1) + sum([x//2 for x in l]))