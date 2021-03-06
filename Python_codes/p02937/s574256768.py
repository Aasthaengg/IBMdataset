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

def main():
    s = input()
    ls = len(s)
    t = input()
    if t[0] in s:
        idx = s.find(t[0])
    else:
        print(-1)
        exit()
    for i in t[1::]:
        nt = s.find(i,idx%ls+1)
        ntl = s.find(i)
        if ntl == -1:
            print(-1)
            exit()
        elif nt == -1:
            idx = (idx//ls)*ls+ls+ntl
        else:
            idx = (idx//ls)*ls+nt
    print(idx+1)
    return None

if __name__ == '__main__':
    main()
