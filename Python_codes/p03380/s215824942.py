# import numpy as np
import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial, gcd
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10 ** 7)
enu = enumerate
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep="\n")

N = int(input())
A = list(map(int, input().split()))

fact = [1]
for i in range(1, N + 10):
    fact.append(fact[-1] * i % MOD)


def rev(x):
    return pow(x, MOD - 2, MOD)


def cmb(i, k):
    if i < k:
        return 0
    return fact[i] * rev(fact[k]) * rev(fact[i - k]) % MOD


A.sort()
if N == 2:
    print(A[1], A[0])
    exit()

mv = A[-1]
vm = mv // 2
bli = bisect_left(A, vm)
if bli == N - 1:
    print(mv, A[bli - 1])
elif bli == 0:
    print(mv, A[bli])
else:
    if vm - A[bli - 1] < A[bli] - vm:
        print(mv, A[bli - 1])
    else:
        print(mv, A[bli])

