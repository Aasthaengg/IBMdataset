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

A, B = MAP()

masu = []
for i in range(50):  # 上が白
	masu.append(["#"]*100)
for i in range(50):  # 下が黒
	masu.append(["."]*100)

row = 0
column = 0
for i in range(A-1):
	masu[row][column] = "."
	column += 2
	if column >= 100:
		column = 0
		row += 2

row = -1
column = 0
for i in range(B-1):
	masu[row][column] = "#"
	column += 2
	if column >= 100:
		column = 0
		row -= 2

print(100, 100)
for i in range(100):
	print(*masu[i], sep="")
