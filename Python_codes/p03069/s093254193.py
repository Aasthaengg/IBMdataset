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
    N = int(input())
    S = input()
    n_white = [0] * (N+1)
    black_position = []
    for i in range(N-1, -1, -1):
        n_white[i] = n_white[i+1]
        if S[i] == '#':
            black_position.append(i)
        else:
            n_white[i] += 1
    #print(black_position)
    #print(n_white)
    ans = min(len(black_position), N - len(black_position))
    for p, k in enumerate(black_position[::-1]):
        ans = min(ans, p + n_white[k])

    print(ans)

if __name__ == "__main__":
    run()