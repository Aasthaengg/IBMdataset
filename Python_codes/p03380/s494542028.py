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
import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque

INF = 1 << 50

def run():
    n = int(sysread())
    A = list(map(int, sysread().split()))
    #print(A)
    A = sorted(A)
    #print(n, A)
    idx = bisect.bisect_left(A, A[-1] / 2)
    if idx == 0:
        print(f'{A[-1]} {A[0]}')
    elif idx == n-1:
        print(f'{A[-1]} {A[-2]}')
    else:
        val1 = A[idx]
        val2 = A[idx-1]
        if abs(val1 - A[-1] / 2) > abs(val2 - A[-1] / 2):
            print(f'{A[-1]} {val2}')
        else:
            print(f'{A[-1]} {val1}')


if __name__ == "__main__":
    run()