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


N, K = map(int, input().split())
mod = 10**9+7
c = Combi(4*10**5+100, mod)
if N <= K:
    print(c.com(2*N-1, N-1))
else:
    ans = c.com(2*N-1, N-1)
    for i in range(K+1, N):
        ans -= c.com(N-1, N-i-1)*c.com(N, i)
    print(ans % mod)