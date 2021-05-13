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

cnt = 0
tmp = False
for i in range(1, len(S)):
	if tmp:
		tmp = False
	elif S[i] == S[i-1]:
		cnt += 1
		tmp = True

if tmp or S[0] != S[-1]:
	print(cnt*K)
	exit()

cnt2 = 1
tmp = True
for i in range(1, len(S)):
	if tmp:
		tmp = False
	elif S[i] == S[i-1]:
		cnt2 += 1
		tmp = True

if tmp:
	print((cnt+cnt2)*(K//2) + cnt*(K%2))
else:
	print(cnt+cnt2*(K-1))


