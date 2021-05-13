import sys
from bisect import *
from heapq import *
from collections import *
from itertools import *
from functools import *
from math import *
from fractions import *

sys.setrecursionlimit(100000000)
input = lambda: sys.stdin.readline().rstrip()

def main():
    A, B, Q = map(int, input().split())
    s, t = [], []
    for _ in range(A):
        s.append(int(input()))
    for _ in range(B):
        t.append(int(input()))
    for _ in range(Q):
        x = int(input())
        i = bisect_left(s, x)
        j = bisect_left(t, x)
        # visit s[i - 1] or s[i]
        # visit t[j - 1] or t[j]
        s_candidates = [s[k] for k in [i - 1, i] if 0 <= k < A]
        t_candidates = [t[k] for k in [j - 1, j] if 0 <= k < B]
        ans = float('inf')
        for s_candidate in s_candidates:
            for t_candidate in t_candidates:
                right = max(x, s_candidate, t_candidate) - x
                left = x - min(x, s_candidate, t_candidate)
                ans = min(ans, min(right, left) * 2 + max(right, left))
        print(ans)






main()
