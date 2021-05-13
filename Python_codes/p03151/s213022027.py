"""
import random
import functools
import copy
import bisect
import array
import re
import collections
import heapq
import fractions
import itertools
import string
import math
from operator import itemgetter as ig
from bisect import bisect_left, bisect_right, insort_left, insort_right
from itertools import permutations, combinations, product, accumulate, groupby
from heapq import heappush, heappop
from collections import deque, defaultdict, Counter
import sys
sys.setrecursionlimit(10 ** 7)
# import numpy as np

inf = 10 ** 20
INF = float("INF")
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)]
ddn9 = ddn + [(0, 0)]
'''for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:'''
"""

import sys


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    D = []
    S = 0
    cnt = 0
    for i in range(N):
        d = B[i] - A[i]
        if d > 0:
            S += d
            cnt += 1
        else:
            D.append(-d)
            if len(D) == N:
                print(0)
                sys.exit()
    D.sort()
    ans = 0
    for i in range(len(D)-1, -1, -1):
        ans += 1
        if D[i] < S:
            S -= D[i]
            if i == 0:
                if S > 0:
                    print(-1)
                    sys.exit()
        else:
            break
    print(ans + cnt)


if __name__ == '__main__':
    main()
