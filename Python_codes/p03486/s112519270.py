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

S = list(input())
T = list(input())

S.sort()
T.sort(reverse=True)
for s, t in zip(S, T):
    if ord(s) < ord(t):
        # print(ord(s), ord(t))
        print("Yes")
        exit()
    elif ord(s) > ord(t):
        # print(ord(s), ord(t))
        print("No")
        exit()
else:
    if len(S) < len(T):
        print("Yes")
    else:
        print("No")
