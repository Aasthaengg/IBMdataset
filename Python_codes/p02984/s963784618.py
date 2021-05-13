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


def run():
    N = int(sysread())
    A = list(map(int, sysread().split()))
    X = []
    k = 1
    S = 0
    for a in A:
        S += a * k
        k *= -1
    X.append(S)
    for a in A[:-1]:
        X.append(a * 2 - X[-1])
    print(' '.join([str(x) for x in X]))
if __name__ == "__main__":
    run()