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
    N, K = map(int, sysread().split())

    ans = 0
    if not K % 2:
        val = (N - K //2) // K + 1
        val = val ** 3
        ans += val

    val = N // K
    val = val ** 3
    ans += val
    print(ans)
if __name__ == "__main__":
    run()
