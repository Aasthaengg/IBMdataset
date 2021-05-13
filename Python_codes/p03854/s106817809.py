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

def dfs(n,seq):
    if seq[n:] in ['dreamer', 'dream', 'erase', 'eraser']:
        return True

    if seq[n:n+7] == 'dreamer':
        if dfs(n+5, seq):
            return True
        elif dfs(n+7, seq):
            return True
        else:
            return False

    elif seq[n:n+5] == 'dream':
        return dfs(n+5, seq)

    elif seq[n:n+6] == 'eraser':
        return dfs(n+6, seq)

    elif seq[n:n+5] == 'erase':
        return dfs(n+5, seq)
    else:
        return False


def run():
    S = input()
    if dfs(0,S):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    run()