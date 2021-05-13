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

d = defaultdict(int)
for a in A:
    d[a] += 1
cnt = 0
for key, val in d.items():
    if key <= val:
        cnt += val - key
    else:
        cnt += val
print(cnt)
