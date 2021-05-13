import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
import fractions
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    a,b = map(int,ipt().split())
    g = fractions.gcd(a,b)

    #素因数分解
    def factorization(n):
        d = dict()
        ni = n
        pn = 2
        t = 0
        while pn**2 <= n and ni > 1:
            if ni%pn == 0:
                t += 1
                ni //= pn
            else:
                if not t == 0:
                    d[pn] = t
                    t = 0
                if pn == 2:
                    pn = 3
                else:
                    pn += 2
        if t > 0:
            d[pn] = t
        if ni > 1:
            d[ni] = 1
        return d

    d = factorization(g)
    print(len(d.keys())+1)
    return

if __name__ == '__main__':
    main()
