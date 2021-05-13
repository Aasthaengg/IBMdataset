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
    N, K, *A = map(int, read().split())
    A_lists = [A]
    while True:
        generated_A = []
        B = A_lists[-1]
        for i in range(0, len(B), 2):
            if i+1 < len(B):
                val = math.gcd(B[i], B[i+1])
                generated_A.append(val)
            else:
                generated_A.append(B[i])
        A_lists.append(generated_A)
        if len(generated_A) == 1:
            break

    gcd = A_lists[-1][0]
    #print(gcd)
    amax = max(A)
    if not K % gcd and K <= amax:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')



if __name__ == "__main__":
    run()