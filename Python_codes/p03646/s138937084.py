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
    t = k//50
    rs = k%50
    print(50)
    ans = []
    for i in range(rs):
        ans.append(str(100-rs+t))
    for i in range(50-rs):
        ans.append(str(49-rs+t))

    print(" ".join(ans))

    return None

if __name__ == '__main__':
    main()
