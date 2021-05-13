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
mod = 10**9+7 #998244353
dir = [(-1,0),(1,0),(0,-1),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"

def main():
    n,k = map(int,ipt().split())
    v = [int(i) for i in ipt().split()]
    rv = v[::-1]
    ma = 0
    for ai in range(n+1):
        for bi in range(n-ai+1):
            d = k-ai-bi
            if d < 0:
                continue
            vs = v[:ai:]+rv[:bi:]
            vs.sort(reverse=True)
            for i in range(min(ai+bi,d)):
                if vs[-1] >= 0:
                    break
                else:
                    vs.pop()
            nm = sum(vs)
            if ma < nm:
                ma = nm

    print(ma)



    return None

if __name__ == '__main__':
    main()
