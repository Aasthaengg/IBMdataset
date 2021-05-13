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



def run():
    sx, sy, tx, ty = map(int, sysread().split())

    ans = ''
    ans += 'R' * (tx-sx)
    ans += "U" * (ty-sy)
    ans += "L" * (tx-sx)
    ans += 'D' * (ty-sy)
    ans += "D"
    ans += 'R' * (tx-sx+1)
    ans += 'U' * (ty-sy+1)
    ans += 'L'
    ans += 'U'
    ans += 'L' * (tx-sx+1)
    ans += 'D' * (ty-sy+1)
    ans += 'R'
    print(ans)


if __name__ == "__main__":
    run()