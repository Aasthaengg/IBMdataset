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
    s = input()
    st = set(s)
    mi = 10**18
    for i in st:
        ma = 0
        nr = 0
        for j in s:
            if j == i:
                if ma < nr:
                    ma = nr
                nr = 0
            else:
                nr += 1
        if nr > ma:
            ma = nr
        if mi > ma:
            mi = ma
    print(mi)

    return

if __name__ == '__main__':
    main()
