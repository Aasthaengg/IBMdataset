import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd, atan2
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

N = INT()
AB = [LIST() for _ in range(N)]

zero = 0
tmp = []
dic = defaultdict(lambda: [0, 0])

for x, y in AB:
	if x == 0 and y == 0:
		zero += 1
	else:
		g = gcd(x, y)
		x //= g
		y //= g
		if y < 0: x *= -1; y *= -1
		if y == 0 and x < 0: x *= -1; y *= -1

		rot90 = (x <= 0)
		if rot90:
			x, y = y, -x
		if rot90:
			dic[(x, y)][0] += 1
		else:
			dic[(x, y)][1] += 1

ans = 1
for l in dic.values():
	ans *= (pow(2, l[0], mod)-1 + pow(2, l[1], mod)-1 + 1)
	ans %= mod

ans -= 1
ans += zero
print(ans%mod) 
