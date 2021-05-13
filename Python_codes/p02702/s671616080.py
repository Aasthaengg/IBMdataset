import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    s = list(map(int,input()))[::-1]
    d = defaultdict(int)
    ans = 0
    ni = 0
    mod = 2019
    d[0] = 1
    n10 = 1
    for i in s:
        ni = (ni+i*n10)%mod
        d[ni] += 1
        n10 = (n10*10)%mod
    for i in d.values():
        ans += i*(i-1)//2
    print(ans)

    return

if __name__ == '__main__':
    main()
