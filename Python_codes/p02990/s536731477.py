
class FermatCombination():
    def __init__(self, size, mod):
        self.mod = mod
        self.factrial = [1]
        self.inverse = [1]
        for i in range(1, size + 1):
            self.factrial.append((self.factrial[i-1]*i) % self.mod)
            self.inverse.append(self.modpow(self.factrial[i], self.mod - 2) % self.mod)

    def modpow(self, x, n):
        ret = 1
        while(n > 0):
            if n & 1:
                ret = ret * x % self.mod
            x = x * x % self.mod
            n >>= 1
        return ret

    def combine(self, n, k):
        return self.factrial[n] * self.inverse[k] % self.mod * self.inverse[n - k] % self.mod


N, K = map(int, input().split())
mod = 10**9+7

fermat = FermatCombination(N + 2, mod)

for i in range(1, K+1):
    if N-K+1 < i:
        print(0)
    else:
        print(fermat.combine(N-K+1, i) * fermat.combine(K-1, i-1) % mod)


