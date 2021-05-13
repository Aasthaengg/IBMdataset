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
    N = int(sysread())
    A = list(map(int, sysread().split()))
    B = list(map(int, sysread().split()))
    C = list(map(int, sysread().split()))
    A.sort()
    B.sort()
    C.sort()
    ansBa = []
    ansBc = []
    for i in range(N):
        b = B[i]
        idx = bisect.bisect_left(A, b)
        ansBa.append(idx)

        idx2 = bisect.bisect_right(C, b)
        ansBc.append(N-idx2)

    #print(ansBc, ansBa)
    ans = 0
    for aa, cc in zip(ansBa, ansBc):
        ans += aa * cc


    print(ans)

if __name__ == "__main__":
    run()
