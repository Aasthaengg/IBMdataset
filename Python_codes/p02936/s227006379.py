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

INF = 1 << 50

def dfs(current, node_vals, seen, to):
    for next in to[current]:
        if not seen[next]:
            node_vals[next] += node_vals[current]
            seen[next] = 1
            dfs(next, node_vals, seen, to)


def run():
    N, Q = map(int, sysread().split())
    to = [[] for _ in range(N+1)]
    for i in range(N-1):
        a,b = map(int, sysread().split())
        to[a].append(b)
        to[b].append(a)

    node_vals = [0] * (N+1)

    for i in range(Q):
        p, x = map(int, sysread().split())
        node_vals[p] += x

    seen = [0] * (N+1)
    seen[1] = 1
    dfs(1, node_vals, seen, to)

    node_vals = [str(v) for v in node_vals]
    print(' '.join(node_vals[1:]))

if __name__ == "__main__":
    run()