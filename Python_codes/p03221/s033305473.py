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

INF = 1 << 50


def run():
    N,M, *PY = map(int, read().split())
    PY = [(PY[2 * i + 1], PY[2 * i], i) for i in range(M)]

    count_town = [0] * (N+1)
    ans = [''] * M
    PY = sorted(PY)
    for y, p, i in PY:
        count_town[p] += 1
        right = count_town[p]
        left = p
        right = (6- len(str(right))) * '0' + str(right)
        left = (6 - len(str(left))) * '0' + str(left)
        ans[i] = left + right

    for a in ans:
        print(a)






if __name__ == "__main__":
    run()