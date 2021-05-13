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

INF = 1 << 50



def run():
    N, *A = map(int, read().split())

    SUM = sum([abs(a) for a in A])
    if A.count(0):
        print(SUM)
        return

    do = [0]
    for a in A[:-1]:
        if not do[-1]:
            if a > 0:
                do.append(0)
            else:
                do.append(1)
        else:
            if a > 0:
                do.append(1)
            else:
                do.append(0)

    if A[-1] > 0:
        if do[-1]:
            base_ans = SUM - abs(A[-1]) * 2
        else:
            print(SUM)
            return
    else:
        if do[-1]:
            print(SUM)
            return
        else:
            base_ans = SUM - abs(A[-1]) * 2
    ans = base_ans
    for i in range(N-1):
        ans = max(ans, base_ans - abs(A[i]) * 2 + abs(A[-1]) * 2)

    print(ans)





if __name__ == "__main__":
    run()