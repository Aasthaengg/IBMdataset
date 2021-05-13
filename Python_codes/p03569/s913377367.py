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
    S = input()

    l = 0
    r = len(S) - 1

    ans = 0
    while l < r:
        if S[l] == S[r]:
            l+=1
            r-=1
        elif S[l] == 'x':
            l += 1
            ans += 1
        elif S[r] == 'x':
            r -= 1
            ans += 1
        else:
            print(-1)
            return
    print(ans)

if __name__ == "__main__":
    run()