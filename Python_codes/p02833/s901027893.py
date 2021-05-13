# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import product, accumulate, combinations, product
#import bisect# lower_bound etc
#import numpy as np
#from copy import deepcopy
#from collections import deque

def run():
    N = int(input())
    if N % 2:
        print(0)
    else:
        ans = 0
        div = 10
        while True:
            val = N // div
            ans += val
            if not val:break
            div *= 5
        print(ans)

if __name__ == "__main__":
    run()