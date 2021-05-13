import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
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

N, C = MAP()
x = [0] * N
v = [0] * N
for i in range(N):
	x[i], v[i] = MAP()

A = [0] * N
v_tmp = 0
for i in range(N):
	v_tmp += v[i]
	A[i] = v_tmp - x[i]

B = [0] * N
v_tmp = 0
for i in range(N-1, -1, -1):
	v_tmp += v[i]
	B[i] = v_tmp - (C-x[i])

gA = [0] * N
gA[0] = A[0]
for i in range(1, N):
	gA[i] = max(gA[i-1], A[i])

gB = [0] * N
gB[N-1] = B[N-1]
for i in range(N-2, -1, -1):
	gB[i] = max(gB[i+1], B[i])

a = max(A)
b = max(B)
c, d = 0, 0
if N > 1:
	c = max([A[i]-x[i]+gB[i+1] for i in range(N-1)])
	d = max([B[i]-(C-x[i])+gA[i-1] for i in range(N-1, 0, -1)])

print(max(a, b, c, d, 0))
