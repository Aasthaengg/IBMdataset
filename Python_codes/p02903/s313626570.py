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
    H, W, A, B = map(int, sysread().split())
    MAP = [[0] * W for _ in range(H)]


    for i in range(H):
        for j in range(W):
            if (0 <= i <= B-1 and 0 <= j <= A-1) or (B <= i and A <= j):
                MAP[i][j] = 1


    for m in MAP:
        print(''.join([str(s) for s in m]))

if __name__ == "__main__":
    run()
