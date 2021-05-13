class Factorial():
    def __init__(self, n, mod):
        self.mod = mod
        self.factorial = [0 for _ in range(n + 1)]
        self.inv = [0 for _ in range(n + 1)]
        self.factorial[0] = 1
        self.inv[0] = 1
        for i in range(n):
            self.factorial[i + 1] = self.factorial[i] * (i + 1) % mod
        self.inv[n] = pow(self.factorial[n], mod - 2, mod)
        for i in range(n)[::-1]:
            self.inv[i] = self.inv[i + 1] * (i + 1) % mod

    def fact(self, m):
        return self.factorial[m]

    def invfact(self, m):
        return self.inv[m]

    def perm(self, m, k):
        if m < k: return 0
        return self.factorial[m] * self.inv[m - k] % self.mod

    def comb(self, m, k):
        if m < k: return 0
        return self.factorial[m] * self.inv[k] * self.inv[m - k] % self.mod

    def hcomb(self, m, k):
        if m + k == 0: return 1
        return self.comb(m + k - 1, k)


N, A, B = map(int, input().split())
V = list(map(int, input().split()))

V.sort(reverse=True)

F = Factorial(100, 100000000000000000039)

res = 0
num = 1
val = 0

for n in range(A, B + 1):
    v = 0
    for i in range(n):
        v += V[i]
    m = 0
    k = 0
    for i in range(N):
        if V[i] == V[n - 1]:
            m += 1
            if i > n - 1:
                k += 1
    if val * n < v * num:
        res = F.comb(m, k)
        num = n
        val = v
    elif val * n == v * num:
        res += F.comb(m, k)
    else:
        pass

print(val / num)
print(res)