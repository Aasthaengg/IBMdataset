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
        return self.fac[n] * self.pow(self.fac[n-r], MOD-2) % MOD

def main():
    N, K = list(map(int, input().split()))
    g = [[] for i in range(N+1)]
    ans = K

    for i in range(N-1):
        a, b = list(map(int, input().split()))
        g[a].append(b)
        g[b].append(a)

    comb = Comb(K)

    q = deque([(-1, 1)])
    while q:
        par, chi = q.pop()
        r = len(g[chi])-1
        if par == -1: k = K-1; r += 1
        else: k = K-2
        if k < r: ans = 0; break

        ans = ans * comb.permutation(k, r) % MOD
        for c in g[chi]:
            if c != par: q.append((chi, c))

    print(ans%MOD)
    
if __name__ == '__main__':
    main()
