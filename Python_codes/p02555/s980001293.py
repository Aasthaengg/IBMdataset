#!/usr/bin python3
# -*- coding: utf-8 -*-

mod = 10**9+7

N = 10**6                   # 出力の制限
g1 = [1]*(N+1)              # 元テーブル
g2 = [1]*(N+1)              # 逆元テーブル
for i in range(2, N + 1 ): # 準備
    g1[i] = ( g1[i-1] * i ) % mod
g2[N] = pow(g1[-1], mod-2, mod)
for i in range(N, 0, -1):
    g2[i-1] = ( g2[i] * i ) % mod

def nCr(n, r):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

s = int(input())
ret = 0
for n in range(1,s):
    r = s - n*3
    if r<0:
        break
    ret += nCr(n+r-1,r)  #n+r-1Cr
    ret %= mod
print(ret)
