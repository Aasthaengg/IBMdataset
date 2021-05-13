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
    N = int(sysread())
    XL = []
    for i in range(N):
        x,l = map(int, sysread().split())
        XL.append((x-l, l+x))
    XL = sorted(XL, key = lambda x:x[1])
    #print(XL)
    ans = 0
    pre_end = - (1 << 50)
    for left,right in XL:
        if pre_end <= left:
            ans += 1
            pre_end = right
    print(ans)


if __name__ == "__main__":
    run()