import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
X = [int(input()) for _ in range(Q)]

def bound(Z, z):
    l = 0
    r = len(Z) - 1
    while r - l > 1:
        m = (l + r) // 2
        if Z[m] >= z:
            r = m
        else:
            l = m
    return r

for x in X:
    s = [0] * 2
    s[0] = bound(S, x)
    s[1] = s[0] - 1

    t = [0] * 2
    t[0] = bound(T, x)
    t[1] = t[0] - 1

    ans = INF
    # print("--------------")
    for i in range(2):
        for j in range(2):
            val = 0
            if x >= S[s[i]] and x >= T[t[j]]:
                val = max(abs(x - S[s[i]]), abs(x - T[t[j]]))
            elif x <= S[s[i]] and x <= T[t[j]]:
                val = max(abs(x - S[s[i]]), abs(x - T[t[j]]))
            else:
                val = min(abs(x - S[s[i]]) * 2 + abs(x - T[t[j]]), abs(x - S[s[i]]) + abs(x - T[t[j]]) * 2)
            ans = min(ans, val)
    # print(x)
    # print(S[s[0]], S[s[1]])
    # print(T[t[0]], T[t[1]])
    # print("--------------")
    print(ans)

    # print(S[s1], S[s2], T[t1], T[t2], T[t3], T[t4])
    # val1 = abs(S[s1] - x) + abs(T[t1] - S[s1])
    # val2 = abs(S[s1] - x) + abs(T[t2] - S[s1])
    # val3 = abs(S[s2] - x) + abs(T[t3] - S[s2])
    # val4 = abs(S[s2] - x) + abs(T[t4] - S[s2])
    # print(min(val1, val2, val3, val4))