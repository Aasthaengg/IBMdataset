def prepare(n):
    global MOD
    modFacts = [0] * (n + 1)
    modFacts[0] = 1
    for i in range(n):
        modFacts[i + 1] = (modFacts[i] * (i + 1)) % MOD

    invs = [1] * (n + 1)
    invs[n] = pow(modFacts[n], MOD - 2, MOD)
    for i in range(n, 1, -1):
        invs[i - 1] = (invs[i] * i) % MOD

    return modFacts, invs


MOD = 10 ** 9 + 7
K = int(input())
S = input()
L = len(S)
modFacts, invs = prepare(K + L)

ans = 0
for n in range(L, L + K + 1):
    nonSi = (pow(25, n - L, MOD) * pow(26, L + K - n, MOD)) % MOD
    Si = (modFacts[n - 1] * invs[L - 1] * invs[n - 1 - (L - 1)]) % MOD
    ans += nonSi * Si
    ans %= MOD

print(ans)
