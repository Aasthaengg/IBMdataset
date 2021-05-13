n, k = map(int, input().split())

MOD = 10 ** 9 + 7

class ModCmb:
    def __init__(self, size):
        self.inv = [1] * (size + 1)
        self.fact = [1] * (size + 1)
        temp_inv = [1] * (size + 1)
        for i in range(2, size + 1):
            temp_inv[i] = ( -(MOD // i) * temp_inv[MOD%i] ) % MOD
        for i in range(2, size + 1):
            self.fact[i] = self.fact[i-1] * i % MOD
            self.inv[i] = self.inv[i-1] * temp_inv[i] % MOD

    def cmb(self, n, r):
        if n <= 1 or n == r:
            return 1
        elif r == 1:
            return n
        else:
            return  (self.fact[n] * self.inv[r] % MOD ) * self.inv[n-r] % MOD

mc = ModCmb(n)

ans = n * (n-1) + 1

for m in range(2, min(n, k+1)):
    ans = ( ans + ((mc.cmb(n, m) % MOD) * mc.cmb(n-1, m)) % MOD ) % MOD

print(ans)