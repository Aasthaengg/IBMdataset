def prepare(n, MOD):

    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv

    return factorials, invs


k = int(input())
s = input()
length = len(s)
MOD = 10**9 + 7

fact, inv = prepare(k + length, MOD)

ans = 0

for i in range(length, length + k + 1):
    coef = fact[i - 1] * inv[i - length] * inv[length - 1] % MOD
    ans += coef * pow(25, i - length, MOD) * pow(26, length + k - i, MOD) % MOD

print(ans % MOD)