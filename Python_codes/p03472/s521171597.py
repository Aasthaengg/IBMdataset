# -*- coding: utf-8 -*-
import numpy as np
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
from scipy.special import comb
import copy
sys.setrecursionlimit(10**6)


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()[:-1]


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


N, H = zz()
A, B = [0] * N, [0] * N

for i in range(N):
    A[i], B[i] = zz()
normal_atack = max(A)

# 投げるだけで倒せるかどうか
sorted_B = sorted(B, reverse=True)
sum_B = [0]*N
sum_B[0] = sorted_B[0]
damege = 0
atack_num = 0
throw_damage = 0
ans = (-(-H // normal_atack))
# print("===========-")
for i in range(0, N):
    throw_damage += sorted_B[i]
    rest_H = H - throw_damage
    if (rest_H <= 0):
        ans = min(i+1, ans)
    else:
        ans = min(-(-rest_H // normal_atack)+i+1, ans)
    # print(ans, throw_damage)
    if (throw_damage >= H):
        break
print(ans)
