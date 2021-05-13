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

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

res = [A[0]]
for a in A[1:]:
    res.append(a)
    res.append(a)
print(sum(res[: N - 1]))
