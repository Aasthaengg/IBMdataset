import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, atan, degrees
from itertools import permutations, combinations, product, accumulate
# とけてない
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect
import heapq

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, M = MAP()
A = LIST()
A.sort(reverse=True)
B = [-x for x in A]

l = 0
r = 2*10**5+1

ans = 0

def count(x):  # 和がx以上になる組み合わせの個数
	cnt = 0
	for y in A:  # 左手
		left = -(x-y)
		cnt += bisect(B, left)

	return cnt

while l+1 != r:
	m = (l+r)//2
	if count(m) < M:
		r = m
	else:
		l = m
ans = 0

A_acc = list(accumulate([0]+sorted(A, reverse=True)))
cnt = 0
for y in A:
	left = -(l-y)
	idx = bisect(B, left)
	ans += A_acc[idx]+idx*y
	cnt += idx
ans -= (cnt-M)*l

print(ans)
