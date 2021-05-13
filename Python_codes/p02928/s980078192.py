import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product, groupby
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


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
    def sum(self, i):  # 区間 [1, i]の和
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    def add(self, i, x):  # iにxを加算
        while i <= self.size:
            self.tree[i] += x
            i += i & -i  
    def pos(self, idx):  # idxの値を取得
        return self.sum(idx) - self.sum(idx-1)
    def lower_bound(self, w):  # w以上の値を持つ最小のidxを検索
        if w <= 0:
            return 0
        idx = 0
        k = 1
        while k*2 <= self.size:
            k *= 2
        while k > 0:
            if idx+k <= self.size and self.tree[idx+k] < w:
                w -= self.tree[idx+k]
                idx += k
            k //= 2
        return idx+1

N, K = MAP()
A = LIST()

bit = Bit(max(N, max(A)))
inv = 0
for i, a in enumerate(A):
	inv += i-bit.sum(a)
	bit.add(a, 1)
ans = inv*K%mod

cnt = [0]*(max(A)+1)
for a in A:
	for b in A:
		if a < b:
			cnt[a] += 1

for n in cnt:
	ans += n*((K*(K-1))//2)
	ans %= mod
print(ans)
