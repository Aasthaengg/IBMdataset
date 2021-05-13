import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
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
xyh = [LIST() for _ in range(N)]

for x, y, h in xyh:
	if h >= 1:
		tmp = (x, y, h)

for i in range(101):
	for j in range(101):
		x_, y_, h_ = tmp
		H = h_ + abs(i-x_) + abs(j-y_)

		for x, y, h in xyh:
			if max(H-abs(x-i)-abs(y-j), 0) != h:
				break
		else:
			print(i, j, H)
			exit()
