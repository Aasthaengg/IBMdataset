K = int(input())
S = input().strip()

MOD = 10 ** 9 + 7

ans = 0

fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]


def cmb(n, k, p):
    global fact, factinv
    if (k < 0) or (n < k):
        return 0
    r = min(k, n - k)
    return fact[n] * factinv[k] * factinv[n - k] % p


N = 2 * 10 ** 6
for i in range(2, N + 10):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)


for i in range(K + 1):
    ans += pow(25, i, MOD) * cmb(i + len(S) - 1, len(S) - 1, MOD) * pow(26, K - i, MOD)
    ans %= MOD

print(ans)