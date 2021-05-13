import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n = int(ipt())
    l = 0
    r = n
    print(0)
    la = input()
    if la == "Vacant":
        exit()
    ra = la
    while True:
        mid = l+(r-l)//2
        print(mid)
        ma = input()
        if ma == "Vacant":
            exit()
        elif (ma == la and (mid-l)%2 == 0) or ((not ma == la) and (mid-l)%2 == 1):
            l = mid
            la = ma
        else:
            r = mid
            ra = ma

    return

if __name__ == '__main__':
    main()
