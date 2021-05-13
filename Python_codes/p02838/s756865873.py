import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log2
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
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
mod = 10 ** 9 + 7

N = INT()
A = LIST()

n = max(A).bit_length()

cnt = [[0, 0] for _ in range(n)]

for x in A:
	x = "{:b}".format(x).zfill(n)
	for i in range(n):
		cnt[i][int(x[-(i+1)])] += 1

ans = 0

for i in range(n):
	bit_sum = ((cnt[i][0]*cnt[i][1])%mod) * pow(2, i, mod) % mod
	ans = (ans+bit_sum)%mod

print(ans)
