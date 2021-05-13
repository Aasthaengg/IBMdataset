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
#import bisect# lower_bound etc
#import numpy as np
#from copy import deepcopy
#from collections import deque


def run():
    a,b,x = map(int, input().split())
    ans = 0
    if a == 0:
        a += 1
        ans = 1
    ans += b // x - (a-1) // x
    print(ans)

if __name__ == "__main__":
    run()
