# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
EPS = 1e-8


def run():
    N, T , *A = map(int, read().split())
    max_gap = 0
    current_min = (INF, -1)
    pairs = set()
    if A[0] > A[1]:
        down = True
    else:
        down = False
        current_min = (A[0], 0)

    for i in range(N-1):
        if down:
            if A[i] < A[i+1]:
                if current_min[0] > A[i]:
                    current_min = (A[i], i)
                down = False
        else:
            if A[i] > A[i+1]:
                down = True
                gap = A[i] - current_min[0]
                if max_gap == gap:
                    pairs.add((current_min[1], i))
                elif max_gap < gap:
                    max_gap = gap
                    pairs = set()
                    pairs.add((current_min[1], i))
                else:
                    continue
    if not down:
        gap = A[N-1] - current_min[0]
        if max_gap == gap:
            pairs.add((current_min[1], N-1))
        elif max_gap < gap:
            max_gap = gap
            pairs = set()
            pairs.add((current_min[1], N-1))
    print(len(pairs))


if __name__ == "__main__":
    run()