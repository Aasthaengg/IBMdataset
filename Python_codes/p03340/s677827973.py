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


r = 0  # index
cnt = 0
xorv = 0
sumv = 0
for l in range(0, N):
    while r < N and xorv ^ A[r] == sumv + A[r]:
        sumv += A[r]
        xorv ^= A[r]
        r += 1
    # print(l, r)
    cnt += r - l
    if l == r:
        r += 1
    else:
        sumv -= A[l]
        xorv = sumv
print(cnt)
