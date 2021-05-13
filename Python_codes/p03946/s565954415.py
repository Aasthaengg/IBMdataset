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
mod = 10**9+7 #998244353
dir = [(-1,0),(0,-1),(1,0),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"

def main():
    n,t = map(int,ipt().split())
    a = [int(i) for i in ipt().split()]
    bs = []
    mi = a[0]
    for i in a[1::]:
        if mi < i:
            bs.append(i-mi)
        else:
            mi = i
    ma = max(bs)
    cnt = 0
    for i in bs:
        if i == ma:
            cnt += 1

    print(cnt)
    return None

if __name__ == '__main__':
    main()
