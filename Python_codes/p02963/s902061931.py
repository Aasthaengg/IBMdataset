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
    S = int(input())
    x1 = 10 ** 9
    y1 = 1
    if not S % x1:
        x2 = 0
        y2 = S // x1
    else:
        x2 = x1 - (S % x1)
        y2 = S // x1 + 1
    print(0,0,x1,y1,x2,y2)
    #print(x1 * y2 - x2 * y1)

if __name__ == "__main__":
    run()