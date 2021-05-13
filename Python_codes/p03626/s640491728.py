import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, atan, degrees
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
S = input()
S2 = input()

if N == 1:
	print(3)
	sys.exit()
else:
	tmp = ""
	if S[0] == S[1]:
		ans = 6
		mode = 2
	else:
		ans = 3
		mode = 1
	tmp = S[0]
	for i in range(1, N):
		if S[i] == tmp:  # 前と同じ
			mode = 2
		else:  # 切り替わり
			if i != N-1 and S[i] == S[i+1]:
				if mode == 1:
					ans = (ans*2)%mod
				elif mode == 2:
					ans = (ans*3)%mod
			else:
				if mode == 1:
					ans = (ans*2)%mod
				elif mode == 2:
					pass
			mode = 1

		tmp = S[i]

print(ans)
