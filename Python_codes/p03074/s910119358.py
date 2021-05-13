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
    n,k = map(int,ipt().split())
    s = input()
    nms = []
    if s[0] == "0":
        nms.append(0)
        ps = "0"
    else:
        ps = "1"
    st = 1
    for i in s[1::]:
        if i == ps:
            st += 1
        else:
            nms.append(st)
            st = 1
            ps = i
    nms.append(st)
    if s[-1] == "0":
        nms.append(0)
#    print(nms)
    ln = len(nms)
    sm = sum(nms[:min(2*k+1,ln):])
    ma = sm
    for i in range(2*k+2,ln,2):
        sm += nms[i]+nms[i-1]-nms[i-2*k-2]-nms[i-2*k-1]
        if ma < sm:
            ma = sm
    print(ma)

    return None

if __name__ == '__main__':
    main()
