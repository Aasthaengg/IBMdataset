import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

K = INT()
A = LIST()

def f(N):
	left = N
	for a in A:
		left = left//a*a
	return left

l_N_max = 0
r_N_max = K*max(A)+2
while l_N_max+1 < r_N_max:
	m = (l_N_max+r_N_max)//2
	if f(m) <= 2:
		l_N_max = m
	else:
		r_N_max = m

N_max = l_N_max

l_N_min = 0
r_N_min = K*max(A)+2
while l_N_min+1 < r_N_min:
	m = (l_N_min+r_N_min)//2
	if f(m) < 2:
		l_N_min = m
	else:
		r_N_min = m
N_min = r_N_min

if N_min > N_max:
	print(-1)
else:
	print(N_min, N_max)
