'''
研究室PCでの解答
'''
import math
#import numpy as np
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9+7

def main():
    n,a,b = map(int,ipt().split())
    h = [int(ipt()) for i in range(n)]
    l = 1
    r = 10**10
    while l != r:
        mid = l + (r-l)//2
        nm = 0
        for i in h:
            nm += max(0,math.ceil((i-b*mid)/(a-b)))
        if nm > mid:
            l = mid+1
        else:
            r = mid

    print(l)
    return None

if __name__ == '__main__':
    main()
