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
mod = 10 ** 9 + 7

def count(arr, x):
    ans1 = 0
    pre = 0
    N = len(arr)
    for i in range(1, N):
        val = max(0, arr[i - 1] + arr[i] - pre - x)
        if val > arr[i]:
            pre = arr[i]
        else:
            pre = val
        ans1 += val
    return ans1

def run():
    N, x, *A = map(int, read().split())

    print(min(count(A, x), count(A[::-1], x)))

if __name__ == "__main__":
    run()
