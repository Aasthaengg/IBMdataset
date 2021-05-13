mod = 998244353

class mod_combination:
    def __init__(self, N):
        self.fac = [1] * (N + 1)
        for i in range(1, N + 1):
            self.fac[i] = (self.fac[i - 1] * i) % mod
        self.invmod = [1] * (N + 1)
        self.invmod[N] = pow(self.fac[N], mod - 2, mod)
        for i in range(N, 0, -1):
            self.invmod[i - 1] = (self.invmod[i] * i) % mod
        
    def calc(self, n, k): # nCk
        return self.fac[n] * self.invmod[k] % mod * self.invmod[n - k] % mod


n, m, k = map(int, input().split())
C = mod_combination(n)
ans = 0
for x in range(k + 1):
    ans = (ans + C.calc(n - 1, n - x - 1) * m * pow(m - 1, n - x - 1, mod) % mod) % mod
print(ans)
