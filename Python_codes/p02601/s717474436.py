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

def main():
    a,b,c = map(int,ipt().split())
    k = int(ipt())
    t = 0
    while a >= b:
        t += 1
        b *= 2
    while b >= c:
        t += 1
        c *= 2
    if k >= t:
        print("Yes")
    else:
        print("No")

    return None

if __name__ == '__main__':
    main()
