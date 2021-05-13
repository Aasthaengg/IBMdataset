#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1
sys.setrecursionlimit(10**7)

n,k=map(int,input().split())
G=[[] for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    a-=1; b-=1
    G[a].append(b)
    G[b].append(a)

class InverseTable:
    __slots__ = ['In', 'fac', 'Ifac']

    def __init__(self, mod, maxnum):
        self.In = [0, 1]; self.fac = [1, 1]; self.Ifac = [1, 1]
        for i in range( 2, maxnum + 1 ):
            self.In.append( ( -self.In[mod % i] * (mod//i) ) % mod )
            self.fac.append( ( self.fac[-1] * i ) % mod )
            self.Ifac.append( (self.Ifac[-1] * self.In[-1]) % mod )
        
    def cmb(self, n, r):
        if ( r<0 or r>n ): return 0
        r = min(r, n-r)
        return self.fac[n] * self.Ifac[r] * self.Ifac[n-r] % mod
    
    def per(self, n, r):
        if ( r<0 or r>n ): return 0
        return self.fac[n] * self.Ifac[n-r] % mod

invt = InverseTable(mod, 2*10**5)
# maxnum=10**6だとテーブル生成に200ms程かかるので
# 最大生成領域は問題ごとに要検討

def dfs(s,node,parent):
    if len(G[node])>=k: return 0
    elif len(G[node])-s==0: return 1
    # else: result=(invt.fac[k-1-s]*invt.Ifac[k-1-s-(len(G[node])-s)])%mod
    else: result=invt.per(k-1-s,len(G[node])-s)
    for i ,di in enumerate(G[node]):
        if di == parent: continue
        result*=dfs(1,di,node); result%=mod
    # print(node,result)
    return result

print((k*dfs(0,0,-1))%mod)


    

