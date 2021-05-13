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
mod = 10**9+7 #998244353
dir = [(-1,0),(1,0),(0,-1),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"

#xの約数を昇順に列挙 O(√N)
def Enumeration(x):
    low = []
    high = []
    for i in range(1,x):
        if i**2 >= x:
            if i**2 == x:
                low.append(i)
            break
        if x%i == 0:
            low.append(i)
            high.append(x//i)
    return high+low[::-1]  #降順
#    return low+high[::-1]

def main():
    n,k = map(int,ipt().split())
#    n = 500
#    k = 1
#    a = [10**6 for i in range(n)]
    a = [int(i) for i in ipt().split()]
    sm = sum(a)
    ys = Enumeration(sm)

    for i in ys:
        nm = 0
        vs = [j%i for j in a]
        vs.sort()
        l = 0
        r = n-1
        rs = 0
#        print(vs)
        while l <= r:
            if rs == 0:
                rs = vs[l]
                nm += rs
                l += 1
            if l > r:
                break
            if rs+vs[r] >= i:
                rs = rs-(i-vs[r])
                r -= 1
            else:
                vs[r] += rs
                rs = 0
#        print(i,nm,rs)
        if nm <= k and rs == 0:
            print(i)
            exit()


    return None

if __name__ == '__main__':
    main()
