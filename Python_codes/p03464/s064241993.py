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
    k = int(ipt())
    a = [int(i) for i in ipt().split()]
    mi = 2
    ma = 2
    for i in a[::-1]:
        mi = ((mi-1)//i+1)*i
        ma = (ma//i)*i
        if mi > ma:
            print(-1)
            exit()
        ma = ma+i-1
    print(mi,ma)

    return None

if __name__ == '__main__':
    main()
