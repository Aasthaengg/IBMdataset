import math
import numpy as np

def Next(): return input()
def NextInt(): return int(Next())
def NextInts(): return map(int,input().split())
def Nexts(): return map(str,input().split())
def NextIntList(): return list(map(int,input().split()))
def RowInts(n): return [input() for i in range(n)]

def inv(x, mod):
    return pow(x, mod-2, mod)

class combination:
    def __init__(self, n, mod = 10**9 + 7):
        self.MOD = mod
        self.to = np.ones(n,dtype=np.int64)
        self.rev = np.ones(n,dtype=np.int64)
        for i in range(1, n):
            self.to[i] = self.to[i-1] * i % mod
        self.rev[-1] = inv(int(self.to[-1]),mod)
        for i in range(n-1, 0, -1):
            self.rev[i-1] = self.rev[i] * i % mod
    
    def nCk(self, n ,k):
        return self.to[n] * self.rev[k] % self.MOD * self.rev[n-k] % self.MOD

MOD = 998244353

n,m,k = NextInts()

cob = combination(200200, MOD)
ans = 0

x = pow(m-1, n-k-1) * m % MOD
for i in range(k+1):
    ans += x * cob.nCk(n-1, k-i)
    ans %= MOD
    x *= m-1
    x %= MOD

print(ans)