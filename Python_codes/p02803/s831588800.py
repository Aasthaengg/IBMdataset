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
from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50

def bfs(MAZE, start):
    s = start + (0,)
    queue = deque([s])
    max_count = 0
    seen = set()
    seen.add(start)
    while queue:
        y,x,count = queue.popleft()
        max_count = max(max_count, count)
        for i,j in ((0,1), (0,-1), (1,0), (-1, 0)):
            next_y, next_x = y + i, x + j
            #print(next_y, next_x)
            if not (next_y, next_x) in seen and MAZE[next_y][next_x] == '.':
                queue.append((next_y, next_x, count+1))
                seen.add((next_y, next_x))
    return max_count


def run():
    H, W = map(int, input().split())
    MAZE = ['#' * (W+2)]
    for _ in range(H):
        s = input()
        s = '#' + s + '#'
        MAZE.append(s)
    MAZE.append('#' * (W+2))

    #for m in MAZE:
    #    print(m)

    ways = []
    for i in range(1, H+1):
        for j in range(1, W+1):
            if MAZE[i][j] == '.':
                ways.append((i, j))

    max_count = 0
    for s_i, s_j in ways:
        min_count = bfs(MAZE, (s_i, s_j))
        #print((s_i, s_j), '->', (g_i, g_j))
        #print(min_count)
        max_count = max(max_count, min_count)

    print(max_count)

if __name__ == "__main__":
    run()