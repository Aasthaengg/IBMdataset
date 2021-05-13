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

N = INT()

lim = 55555
prime = [1]*(lim+1)
prime[0] = 0
prime[1] = 0

for i in range(lim+1):
	if prime[i] == 1:
		for j in range(2, lim//i + 1):
			prime[i*j] = 0

p = [i for i in range(lim+1) if prime[i]]

ans = [x for x in p if x%5 == 2]
print(*ans[:N])