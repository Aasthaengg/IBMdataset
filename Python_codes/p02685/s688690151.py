mod = 998244353

class Combination:
    def __init__(self, N):
        self.fac = [1] * (N + 1)
        for i in range(1, N + 1):
            self.fac[i] = (self.fac[i - 1] * i) % mod
        self.invmod = [1] * (N + 1)
        self.invmod[N] = pow(self.fac[N], mod - 2, mod)
        for i in range(N, 0, -1):
            self.invmod[i - 1] = (self.invmod[i] * i) % mod

    def calc(self, n, k):  # nCk
        return self.fac[n] * self.invmod[k] % mod * self.invmod[n - k] % mod


N, M, K = map(int, input().split())
C = Combination(N)

ans = 0
for k in range(K + 1):
    tmp = C.calc(N - 1, N - k - 1) * M * pow(M - 1, N - k - 1, mod) % mod
    ans = (ans + tmp) % mod

print(ans)