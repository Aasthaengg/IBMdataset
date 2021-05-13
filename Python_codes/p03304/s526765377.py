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
dir = [(-1,0),(1,0),(0,-1),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"


def main():
    n,m,d = map(int,ipt().split())
    if d == 0:
        print((m-1)/n)
    else:
        print((n-d)*(m-1)*2/(n**2))

    return None

if __name__ == '__main__':
    main()
