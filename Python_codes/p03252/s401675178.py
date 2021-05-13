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

sd = defaultdict(lambda: ".")
td = defaultdict(lambda: ".")

for s, t in zip(S, T):
    if sd[s] != "." and sd[s] != t:
        print("No")
        exit()
    if td[t] != "." and td[t] != s:
        print("No")
        exit()
    sd[s] = t
    td[t] = s
print("Yes")
