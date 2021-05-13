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

N = INT()
T = LIST()
A = LIST()

mountain = [0]*N

h_t = 0
for i in range(N):
	if T[i] != h_t:
		h_t = T[i]
		mountain[i] = T[i]

#print(mountain)
h_a = 0
for i in range(N-1, -1, -1):
	if A[i] != h_a:
		h_a = A[i]
		if mountain[i] == 0:
			mountain[i] = A[i]
		elif mountain[i] != A[i]:
			print(0)
			exit()
	elif h_a < mountain[i]:
		print(0)
		exit()

ans = 1
for i in range(N):
	if mountain[i] == 0:
		ans *= min(T[i], A[i])
		ans %= mod

print(ans)



