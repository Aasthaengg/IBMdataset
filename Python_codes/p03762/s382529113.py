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
    n,m = map(int,ipt().split())
    x = list(map(int,ipt().split()))
    y = list(map(int,ipt().split()))
    mod = 10**9+7

    #nCrをmodで割った余りを求める。Nに最大値を入れて使用。
    N = 10**5
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル
    def cmb(n,r,mod):
        if r<0 or r>n :
            return 0
        r = min(r,n-r)
        return g1[n]*g2[r]*g2[n-r]%mod
    for i in range(2,N+1):
        g1.append((g1[-1]*i)%mod)
        inverse.append((-inverse[mod % i]*(mod//i))%mod)
        g2.append((g2[-1]*inverse[-1])%mod)

    sx = 0
    px = x[0]
    for i,xi in enumerate(x[1:n:]):
        sx = (sx+((xi-px)%mod*(i+1)%mod*(n-i-1))%mod)%mod
        px = xi
    sy = 0
    py = y[0]
    for i,yi in enumerate(y[1:m:]):
        sy = (sy+((yi-py)%mod*(i+1)%mod*(m-i-1))%mod)%mod
        py = yi
    print(sx*sy%mod)


    return

if __name__ == '__main__':
    main()
