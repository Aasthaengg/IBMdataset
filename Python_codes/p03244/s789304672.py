import math
import numpy as np
import queue
from collections import deque,defaultdict
import heapq
from sys import stdin,setrecursionlimit
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
input = stdin.readline
setrecursionlimit(10**7)

def main():
    do = defaultdict(int)
    de = defaultdict(int)
    do[-1] = 0
    de[-1] = 0
    n = int(input())
    v = list(map(int,input().split()))
    for i,vi in enumerate(v):
        if i%2 == 0:
            de[vi] += 1
        else:
            do[vi] += 1
    dem = 0
    demk = 0
    dom = 0
    domk = 0
    for dek,dev in de.items():
        if dem < dev:
            demk = dek
            dem = dev
    for dok,dov in do.items():
        if dom < dov:
            domk = dok
            dom = dov

    if demk == domk:
        if list(do.values()).count(dom) > 1 or list(de.values()).count(dem) > 1:
            print(n-dem-dom)
        else:
            de[demk] = 0
            do[domk] = 0
            dxm = dem
            dem = max(de.values())
            dom = max(do.values())
            if dem > dom:
                print(n-dxm-dem)
            else:
                print(n-dxm-dom)
    else:
        print(n-dem-dom)


if __name__ == '__main__':
    main()
