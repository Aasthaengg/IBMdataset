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
    N, M = map(int, sysread().split())
    A = list(map(int, sysread().split()))
    queue = []
    for a in A:
        heappush(queue, (-a, 1))

    for i in range(M):
        B, C = map(int, sysread().split())
        heappush(queue, (-C, B))
    total = 0
    ans = 0
    while True:
        c, b = heappop(queue)
        c *= -1
        total += b
        if total > N:
            total -= b
            break
        ans += c * b
    ans += (N - total) * c
    print(ans)

if __name__ == "__main__":
    run()