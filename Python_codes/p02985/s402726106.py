import sys
input = sys.stdin.readline
from collections import *

MOD = 10**9+7

class Comb:
    def __init__(self, N):
        self.fac = [1] * (N+1)
        for i in range(2, N+1): self.fac[i] = self.fac[i-1] * i % MOD

    def pow(self, a, b):
        res = 1
        while b:
            if b & 1: res = res * a % MOD
            a = a**2 % MOD
            b >>= 1
        return res

    def comb(self, n, r):
        if r < 0 or r > n: return 0
        return (self.fac[n] * self.pow(self.fac[r], MOD-2)) % MOD * self.pow(self.fac[n-r], MOD-2) % MOD

    def permutation(self, n, r):
        if r == 0: return 1
        return self.fac[n] * self.pow(self.fac[n-r], MOD-2) % MOD

def main():
    N, K = list(map(int, input().split()))
    g = [0] * (N+1)
    
    for i in range(N-1):
        a, b = list(map(int, input().split()))
        g[a] += 1
        g[b] += 1
    
    comb = Comb(K)

    ans = K * comb.permutation(K-1, g[1]) % MOD
    K -= 2
    for i in range(2, N+1):
        if K < g[i]-1: ans = 0; break

        ans = ans * comb.permutation(K, g[i]-1) % MOD

    print(ans%MOD)
if __name__ == '__main__':
    main()
