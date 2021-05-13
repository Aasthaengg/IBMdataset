'''
自宅用PCでの解答
'''
import math
#import numpy as np
import itertools
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
# mod = 998244353
dir = [(-1,0),(0,-1),(1,0),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"
INF = 1<<32-1
# INF = 10**18

def main():
    n,k = map(int,ipt().split())
    if n == 1:
        print(k)
        exit()
    d = [True]*(n+1)
    v = [k-2]*(n+1)
    ans = k*(k-1)
    for i in range(n-1):
        a,b = map(int,ipt().split())
        if d[a]:
            d[a] = False
        else:
            ans *= v[a]
            ans %= mod
            v[a] -= 1
        a = b
        if d[a]:
            d[a] = False
        else:
            ans *= v[a]
            ans %= mod
            v[a] -= 1

    print(ans)

    return None

if __name__ == '__main__':
    main()
