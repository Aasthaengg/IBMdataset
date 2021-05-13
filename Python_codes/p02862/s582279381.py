class Factorials:
    def __init__(self, n=10**6, mod=10**9 + 7):
        self.mod = mod

        # self.fac[i] ≡ i! (factorial:階乗)
        self.fac = [1] * (n+1)
        for i in range(2, n+1):
            self.fac[i] = self.fac[i-1] * i % mod

        # self.rec[i] ≡ 1 / i! (reciprocal:逆数)
        self.rec = [1] * (n+1)
        self.rec[n] = pow(self.fac[n], mod-2, mod)
        for i in range(n-1, 1, -1):
            self.rec[i] = self.rec[i+1] * (i+1) % mod

    # comb(n, r) ≡ nCr
    def comb(self, n, r):
        return self.fac[n] * self.rec[r] * self.rec[n - r] % self.mod

x, y = map(int, input().split())

if (x + y) % 3 != 0:
    print(0)
    exit()
if y < x/2 or 2*x < y:
    print(0)
    exit()

n = (x + y) // 3
r = x - n
c = Factorials(n)
print(c.comb(n, r))
