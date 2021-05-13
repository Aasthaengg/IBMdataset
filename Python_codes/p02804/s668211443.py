import sys
from collections import defaultdict, Counter, namedtuple, deque
import itertools
import functools
import bisect
import heapq
import math

MOD = 10 ** 9 + 7
# MOD = 998244353
# sys.setrecursionlimit(10**8)


class Combination:
    def __init__(self, mod=10**9+7, n=202020):
        self.f = [0] * n
        self.rf = [0] * n
        self.inv = [0] * n
        self.f[0], self.f[1] = 1, 1
        self.rf[0], self.rf[1] = 1, 1
        self.inv[1] = 1
        self.MOD = mod
        for i in range(2, n):
            self.f[i] = (self.f[i - 1] * i) % self.MOD
            self.inv[i] = (-self.inv[self.MOD % i] * (self.MOD // i)) % self.MOD
            self.rf[i] = (self.rf[i - 1] * self.inv[i]) % self.MOD

    def __call__(self, n, r):
        return (self.f[n] * self.rf[r] * self.rf[n - r]) % self.MOD


C = Combination()

n, k = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = 0
for i in range(n-k+1):
    ans = (ans + A[-i-1] * C(n-i-1, k-1)) % MOD
    # print(ans)

for i in range(n-k+1):
    ans = (ans - A[i] * C(n-i-1, k-1)) % MOD
    # print(ans)

print(ans)
