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

s = input()
N = len(s)

t = ""
for X in s:
	if X != "x":
		t += X

if t != t[::-1]:
	print(-1)
	exit()

s2 = s[::-1]

i = 0
j = 0
ans = 0

while i < N and j < N:
	if s[i] == s2[j]:
		i += 1
		j += 1
	else:
		if s[i] == "x":
			i += 1
		else:
			j += 1
		ans += 1

ans += (N - i)*(i < N) + (N - j)*(j < N)

print(ans//2)
