from collections import Counter


MOD = 10 ** 9 + 7


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


def factorization(n):
    arr = Counter()
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr[i] = cnt

    if temp != 1:
        arr[temp] = 1

    if len(arr.keys()) == 0 and n != 1:
        arr[n] = 1

    return arr


N, M = map(int, input().split())
modFacts, invs = prepare(N + 100)
primes = factorization(M)

ans = 1
for p in list(primes.keys()):
    q = primes[p]
    ans *= modFacts[q + N - 1] * invs[q] * invs[N - 1]
    ans %= MOD

print(ans)
