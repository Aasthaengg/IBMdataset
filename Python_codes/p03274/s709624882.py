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
import bisect
import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal

INF = 1 << 50


def run():
    N, K = map(int, sysread().split())
    X = list(map(int, sysread().split()))

    best_time = INF
    for i in range(0, N-K+1):
        left = X[i]
        right =  X[i+K-1]
        if left<=0:
            if right <= 0:
                best_time = min(best_time, abs(left))
            else:
                best_time = min(abs(left) + right + min(abs(left), right), best_time)
        else:
            best_time = min(best_time, right)
            break

    print(best_time)


if __name__ == "__main__":
    run()