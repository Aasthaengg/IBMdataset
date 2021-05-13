# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
import math
#from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7


def run():
    N = int(input())
    for h in range(1, 3501):
        if 4 * h - N <= 0:
            continue
        s = math.ceil(N * h / (4 * h - N))
        for n in range(s, 3501):
            v = N * h * n
            a = 4 * h * n - N * n - N * h
            if a <= 0:continue
            if not v % a:
                w = v // a
                print(f'{h} {n} {w}')
                return

if __name__ == "__main__":
    run()
