k = int(input())
s = input()
MOD = 10**9+7

class Facts():
    # O(max_num)
    def __init__(self, max_num=10**5, p=10**9 + 7):
        self.p = p
        self.max_num = max_num
        self.fact = [1] * (self.max_num + 1)
        for i in range(1, self.max_num + 1):
            self.fact[i] = self.fact[i-1] * i
            self.fact[i] %= self.p

    def comb(self, n, k):
        # nCk mod p with memo
        # O(log(p))
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        a = self.fact[n]
        b = self.fact[k]
        c = self.fact[n-k]
        return (a*self.power_func(b, self.p-2) *
                self.power_func(c, self.p-2)) % self.p

    def power_func(self, a, b):
        # a^b mod p
        # O(log(b))
        ans = 1
        while b > 0:
            if b & 1:
                ans = ans * a % self.p
            a = a * a % self.p
            b >>= 1
        return ans

r26 = [1 for _ in range(k + 1)]
r25 = [1 for _ in range(k + 1)]
for i in range(1, k+1):
   r26[i] = (r26[i-1] * 26) % MOD
   r25[i] = (r25[i-1] * 25) % MOD
facts = Facts(max_num=len(s)+k+1, p=MOD)

total = len(s) + k
ans = 0
for s_n in range(len(s), total+1):
   d = total - s_n
   ans += facts.comb(total - d - 1, len(s) - 1) * r25[k-d] * r26[d]
   ans %= MOD

print(ans)
