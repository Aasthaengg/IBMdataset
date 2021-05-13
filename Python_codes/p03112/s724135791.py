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

'''
pythonにsortedsetをくれlower_boundとupper_boundをくれ
'''

def main():
    a,b,q = map(int,ipt().split())
    s = [-10**11]+[int(ipt()) for i in range(a)]+[10**11]
    t = [-10**11]+[int(ipt()) for i in range(b)]+[10**11]

    for i in range(q):
        x = int(ipt())
        ns = bisect.bisect_left(s,x)
        nt = bisect.bisect_left(t,x)
        ls = s[ns-1]-x
        rs = s[ns]-x
        lt = t[nt-1]-x
        rt = t[nt]-x
        ans = []
        ans.append(2*rs-lt)
        ans.append(2*rt-ls)
        ans.append(max(rs,rt))
        ans.append(-min(ls,lt))
        ans.append(rs-2*lt)
        ans.append(rt-2*ls)
        print(min(ans))

if __name__ == '__main__':
    main()
