from collections import Counter

n, m = map(int, input().split())

MOD = 10 ** 9 + 7

# 素因数分解
power = []
p = 2
mm = m # m をあとで使うので
while mm > 1:
    if mm % p == 0:
        while True:
            if mm % p != 0:
                break
            power.append(p)
            mm //= p
    p += 1

# コンビネーション計算用
fact = [0] * 1100000
invfact = [0] * 1100000

fact[0] = 1
for i in range(1, 1100000):
    fact[i] = fact[i - 1] * i % MOD

# fermat
invfact[1100000 - 1] = pow(fact[1100000 - 1], MOD - 2, MOD)

for i in range(1100000 - 1, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD

def comb(n, k):
    return fact[n] * invfact[k] * invfact[n - k] % MOD

if m == 1:
    print(1)
else:
    res = 1
    c = Counter(power)
    for k, v in c.items():
        res *= comb(v + n - 1, n - 1)
        res %= MOD
    print(res)
