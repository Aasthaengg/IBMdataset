# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
from heapq import heappop, heappush
from collections import defaultdict
sys.setrecursionlimit(10**7)
import math
#from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
from collections import deque
#from decimal import Decimal

INF = 1 << 50

def run():
    K, T, *A = map(int, read().split())
    max_a = max(A)
    print(max(max_a-1-K+max_a, 0))

if __name__ == "__main__":
    run()