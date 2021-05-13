import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, log
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
from decimal import Decimal
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10**9 + 7
from decimal import *

S = input()
N = len(S)+1

ans = [-1]*(N)

for i in range(N-2):
	if S[i] == ">" and S[i+1] == "<":
		ans[i+1] = 0

if S[0] == "<":
	ans[0] = 0

if S[-1] == ">":
	ans[-1] = 0

for i in range(N-1):
	if S[i] == "<" and ans[i] != -1 and ans[i]+1 > ans[i+1] and ans[i+1] != 0:
		ans[i+1] = ans[i] + 1

#print(ans)

for i in range(N-2, -1, -1):
	if S[i] == ">" and ans[i+1] != -1 and ans[i+1]+1 > ans[i] and ans[i] != 0:
		ans[i] = ans[i+1] + 1

#print(ans)
print(sum(ans))