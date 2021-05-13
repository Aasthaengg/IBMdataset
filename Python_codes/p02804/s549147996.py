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
    n,k = map(int,ipt().split())
    a = [int(i) for i in ipt().split()]
    a.sort()
    ra = sorted(a,reverse=True)
    mod = 10**9+7
    ans = 0

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

    for i,ai in enumerate(ra[:n-k+1:]):
        ans = (ans+ai*cmb(n-i-1,k-1,mod))%mod
    for i,ai in enumerate(a[:n-k+1:]):
        ans = (ans-ai*cmb(n-i-1,k-1,mod))%mod
    print(ans)

    return

if __name__ == '__main__':
    main()
