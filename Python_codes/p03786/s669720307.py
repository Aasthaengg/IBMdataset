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
    N, *A = map(int, read().split())
    A = sorted(A)
    B = []
    val = 0
    for a in A:
        val += a
        B.append(val)

    left = -1
    right = -1
    for i in range(N-1):
        if B[i] * 3 >= B[i+1]:
            if left == -1:
                left = i
                right = i+1
            else:
                right = i+1
        else:
            left, right = -1, -1
    print(right - left + 1)


if __name__ == "__main__":
    run()