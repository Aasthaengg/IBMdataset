k = int(input())
s = len(input())
MOD = 10 ** 9 + 7


def mod_inv(n):
    return pow(n, MOD - 2, MOD)

total = pow(26, k + s, MOD)
tmp = pow(25, k + s, MOD)
total = (total - tmp) % MOD

for i in range(0, s-1):
    tmp = ((tmp * ((k+s) - i)) % MOD * mod_inv((i + 1) * 25)) % MOD
    total = (total - tmp) % MOD
print(total)
