# -*- coding: utf-8 -*-
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
import copy
import math
sys.setrecursionlimit(10**6)

# lis_of_lis = [[] for _ in range(N)]


def zz(): return list(map(int, sys.stdin.readline().split()))


def z(): return int(sys.stdin.readline())


def S(): return sys.stdin.readline()[:-1]


def C(line): return [sys.stdin.readline() for _ in range(line)]


MOD = pow(10, 9)+7
N, K = zz()
A = zz()

# Aの中にある転倒数を求める
# Aの中にある転倒数 * K 個転倒数がある
# Aの各要素について、転倒数を求めておけば、それをK倍すればよい

num_tentou = [0] * N
num_tentou_within = [0] * N

for i in range(N):
    base = A[i]
    for j in range(N):
        if (base > A[j]):
            num_tentou[i] += 1
    for j in range(i + 1, N):
        if (base > A[j]):
            num_tentou_within[i] += 1
num = sum(num_tentou)
within_num = sum(num_tentou_within)
ans = -K*(K-1)*num//2 + K*(K-1)*num + within_num*K
print(ans % MOD)
