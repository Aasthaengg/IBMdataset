# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
from heapq import heappop, heappush
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

def count(k, bins, N):
    current = 0
    for i in range(2, N+1):
        if k * i <=N:
            if bins[k*i] == -1:raise ValueError(f'bins{i} is not filled yet')
            current += bins[k*i]
        else:
            break
    return current % 2

def run():
    N = int(sysread())
    A = list(map(int, sysread().split()))
    A = [-1] + A
    bins = [-1] * (N+1)

    for i in range(N, 0, -1):
        bins[i] = (A[i] - count(i, bins, N)) % 2


    print(sum(bins) + 1)
    ans = []
    for i, b in enumerate(bins):
        if b == 1:
            ans.append(str(i))
    print(' '.join(ans))


if __name__ == "__main__":
    run()