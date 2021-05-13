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
A = LIST()[::-1]

if A[0] != 2:
	print(-1)
	exit()

N_min = 2
N_max = 3
for a in A[1:]:
	if ((N_min-1)//a) ==  N_max//a:
		print(-1)
		exit()

	N_min = -(-N_min//a)*a
	N_max = N_max//a*a + a - 1

print(N_min, N_max)
