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
l = 0
r = N-1

print(l, flush=True)
tmp = input()
if tmp == "Vacant":
	exit()

print(r, flush=True)
tmp2 = input()
if tmp2 == "Vacant":
	exit()

while 2 < r-l:
	p = l + (r - l)//2//2*2
	print(p, flush=True)

	Output = input()
	if Output == "Vacant":
		exit()
	elif Output == tmp:
		l = p
	elif Output == tmp2:
		r = p

print(((r+l)//2), flush=True)
Output = input()
if Output == "Vacant":
	exit()