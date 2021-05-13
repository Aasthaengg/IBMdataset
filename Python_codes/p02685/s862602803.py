# -*- coding: utf-8 -*-


class FactMod():
    '''
    modの値が素数の時のfactと組み合わせを求める
    フェルマーの小定理を用いているため、modが素数以外の時は使えない
    '''

    def __init__(self, n, mod):
        '''
        コンストラクタ
        f:nまでの i!の値を　配列に入れる
        inv: (i!)^-1　の値を配列に入れる
        '''
        self.mod = mod
        self.f = [1]*(n+1)
        for i in range(1, n+1):
            self.f[i] = self.f[i-1]*i % mod

        self.inv = [pow(self.f[-1], mod-2, mod)]
        for i in range(1, n+1)[::-1]:
            self.inv.append(self.inv[-1]*i % mod)
        self.inv.reverse()

    def fact(self, n):
        '''
        n!の値を返す
        '''
        return self.f[n]

    def comb(self, n, r):
        '''
        nCrの値を返す
        '''
        ret = self.f[n] * self.inv[n-r]*self.inv[r]
        ret %= self.mod
        return ret

    def perm(self, n, r):
        """
        nPrの値を返す
        """
        ret = self.f[n] * self.inv[n-r]
        ret %= self.mod
        return ret

MOD=998244353
N,M,K = map(int,input().split())

F=FactMod(N+1,MOD)
ans=0
for kk in range(K+1):
    not_kk=N-kk
    if not_kk==0:
        r=M*pow(M-1,N-1,MOD)
        ans+=M*pow(M-1,N-1,MOD)
        ans%=MOD
    else:
        r=M*pow(M-1,not_kk-1,MOD)
        ans+=M*pow(M-1,not_kk-1,MOD)*F.comb(N-1,kk)
        ans%=MOD
print(ans)
