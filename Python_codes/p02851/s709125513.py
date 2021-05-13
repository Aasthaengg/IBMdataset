import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, atan, degrees
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect
import heapq
import numpy as np

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, K = MAP()
A = LIST()

A_acc = list(accumulate(A))
S = [0] + A_acc
S = [(S[i]-i)%K for i in range(N+1)]

ans = 0
dic = defaultdict(int)

for i, x in enumerate(S):
	ans += dic[x]  # 範囲内かつ今まで出てきたxの個数を探す
	dic[x] += 1
	if i >= K-1:  # 範囲外のものを捨てる
		dic[S[i-K+1]] -= 1

print(ans)
