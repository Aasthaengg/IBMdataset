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
EPS = 1e-8
mod = 10 ** 9 + 7
def intread():
    return int(sysread())
def mapline(t = int):
    return map(t, sysread().split())
def mapread(t = int):
    return map(t, read().split())


def run():
    H, W = mapline()
    dic = [0] * 27
    for i in range(H):
        S = input()
        for s in S:
            dic[ord(s) - 96] += 1
    permited2 = 0
    permited1 = 0
    if H % 2 and W % 2:
        permited2 += H // 2 + W // 2
        permited1 += 1
    else:
        if H % 2:
            permited2 += W // 2
        elif W % 2:
            permited2 += H // 2
    permited4 = (H * W - permited2 * 2 - permited1) // 4
    for val in dic:
        done = True
        while val and done:
            done = False
            if val >= 4 and permited4:
                val -= 4
                permited4 -= 1
                done= True
            elif val >= 2 and permited2:
                val -= 2
                permited2 -= 1
                done = True
            elif val == 1 and permited1:
                val -= 1
                permited1 -= 1
                done = True
            if not done:
                print('No')
                return
    print('Yes')


if __name__ == "__main__":
    run()
