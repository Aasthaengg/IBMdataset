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
S = input()

cnt = 0
for num in range(1000):
    snum = str(num).zfill(3)
    # print("snum", snum)
    ind = 0
    chkind = 0
    # while ind < len(S):
    for s in S:
        if chkind >= 3:
            break
        if s == snum[chkind]:
            chkind += 1
    if chkind == 3:
        cnt += 1
print(cnt)