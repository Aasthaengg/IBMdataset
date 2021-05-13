#import math
#import itertools
#import numpy as np
#from collections import deque
# sys.setrecursionlimit(10 ** 6)
mod = 10 ** 9 + 7
#INF = 10 ** 9
#PI = 3.14159265358979323846

INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))



def do():
    def cmb(n, r, mod):
        if ( r<0 or r>n ):
           return 0
        r = min(r, n-r)
        return g1[n] * g2[r] * g2[n-r] % mod

    n,k=INTM()
    r=n-k
    b=k

    N = n
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル

    for i in range( 2, N + 1 ):
        g1.append( ( g1[-1] * i ) % mod )
        inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
        g2.append( (g2[-1] * inverse[-1]) % mod )

    for i in range(1,b+1):
        t1=cmb(r+1,i,mod)
        t2=cmb(b-1,i-1,mod)
        print((t1*t2)%mod)

if __name__=='__main__':
    do()