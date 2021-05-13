import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

n = INT()
a = LIST()

l = [1]*n
l1 = [l[i]*(-1)**i for i in range(n)]
l2 = [l[i]*(-1)**(i+1) for i in range(n)]

ans1 = 0
tmp1 = 0
for i, r in enumerate(a):
	tmp1 += r
	if tmp1*l1[i] <= 0:
		ans1 += abs(tmp1) + 1
		tmp1 = l1[i]

ans2 = 0
tmp2 = 0
for i, r in enumerate(a):
	tmp2 += r
	if tmp2*l2[i] <= 0:
		ans2 += abs(tmp2) + 1
		tmp2 = l2[i]

print(min(ans1, ans2))