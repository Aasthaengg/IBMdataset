# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import product, accumulate, combinations, product
import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7


def run():
    N, *A = map(int, read().split())
    B = [a-k for k, a in enumerate(A, 1)]
    B.sort()
    Bsum = []
    v = 0
    for b in B:
        v += b
        Bsum.append(v)

    min_val = INF
    for k in range(N):
        c = B[k]
        #print(c)
        score = 0
        score -= Bsum[k]
        score += Bsum[-1] - Bsum[k]
        score += -N * c + 2 * c * (k+1)
        #print(score)
        min_val = min(min_val, score)

    print(min_val)


if __name__ == "__main__":
    run()
