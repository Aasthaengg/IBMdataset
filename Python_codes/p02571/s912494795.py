# import numpy as np
import sys, math, heapq
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial, gcd
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep="\n")

S = input()
T = input()
lenS = len(S)
lenT = len(T)

difmin = float("inf")
for si in range(lenS - lenT + 1):
    dif = 0
    for s, t in zip(S[si:], T):
        if s != t:
            dif += 1
    difmin = min(difmin, dif)

print(difmin)
