# coding: utf-8
import sys

# from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
printout = sys.stdout.write
sprint = sys.stdout.flush
# from heapq import heappop, heappush
# from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
# import math
# from itertools import product, accumulate, combinations, product
# import bisect
# import numpy as np
# from copy import deepcopy
from collections import deque

# from decimal import Decimal
# from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7


def intread():
    return int(sysread())
def mapline(t=int):
    return map(t, sysread().split())
def mapread(t=int):
    return map(t, read().split())

def run():
    H, W = mapline()
    A = []
    for i in range(H):
        A.append(list(mapline()))

    output = []
    for i in range(H):
        for j in range(W - 1):
            if A[i][j] % 2:
                A[i][j] -= 1
                A[i][j + 1] += 1
                output.append((i, j, i, j + 1))
    for i in range(H - 1):
        if A[i][W - 1] % 2:
            A[i][W - 1] -= 1
            A[i + 1][W - 1] += 1
            output.append((i, W - 1, i + 1, W - 1))

    print(len(output))
    for i1, j1, i2, j2 in output:
        print(f'{i1 + 1} {j1 + 1} {i2 + 1} {j2 + 1}')


if __name__ == "__main__":
    run()
