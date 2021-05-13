class Cmb:
    def __init__(self, m=10**5, p=10**9+7):
        fct, inv = [1], [1]
        a, b = 1, 1
        for i in range(1, m+1):
            a = (a * i) % p
            b = (b * pow(i, p - 2, p)) % p
            fct.append(a)
            inv.append(b)
        self.fct = fct
        self.inv = inv
        self.p = p

    def calc(self, n, r):
        fct, inv = self.fct, self.inv
        if r < 0 or n < r:
            return 0
        return (fct[n] * inv[r] * inv[n - r]) % self.p


n, k = map(int, input().split())
*A, = map(int, input().split())
A.sort()
s = 0
p = 10**9+7
cmb = Cmb()
for i in range(n):
    s += (A[n-1-i]-A[i])*cmb.calc(n-1-i, k-1)
    s %= p
print(s)
