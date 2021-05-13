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

def run():
    N, H, *AB_ = map(int, read().split())
    AB = []
    for i in range(N):
        a,b = AB_[2*i], AB_[2*i+1]
        AB.append((a, 0, i))
        AB.append((b, 1, i))

    AB = sorted(AB, reverse=True)

    count = 0
    for val, a_b, idx in AB:
        if a_b == 0:
            count += math.ceil(H / val)
            break
        else:
            count += 1
            H -= val
        if H <= 0:
            break
    print(count)

if __name__ == "__main__":
    run()