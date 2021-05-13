# ライブラリ高速化実験テスト
import sys


class Combi():
    def __init__(self, N, mod):
        self.power = [1 for _ in range(N+1)]
        self.rev = [1 for _ in range(N+1)]
        self.mod = mod
        for i in range(2, N+1):
            self.power[i] = (self.power[i-1]*i) % self.mod
        self.rev[N] = pow(self.power[N], self.mod-2, self.mod)
        for j in range(N, 0, -1):
            self.rev[j-1] = (self.rev[j]*j) % self.mod

    def com(self, K, R):
        if K < R:
            return 0
        else:
            return ((self.power[K])*(self.rev[K-R])*(self.rev[R])) % self.mod

    def pom(self, K, R):
        if K < R:
            return 0
        else:
            return (self.power[K])*(self.rev[K-R]) % self.mod



def input(): return sys.stdin.readline().rstrip()


K = int(input())
S = input()
M = len(S)
N = K+M
mod = 10**9+7
ans = pow(26, N, mod)

c = Combi(2*10**6, mod)
for i in range(M):
    ans -= c.com(N, i)*pow(25, N-i, mod)
    ans %= mod
print(ans)