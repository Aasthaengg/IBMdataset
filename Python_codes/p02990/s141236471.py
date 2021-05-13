def combination_init_mod(n, mod):
    fact = [1] * (n + 1)
    inv_fact = [0] * (n + 1)

    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i
        fact[i] %= mod

    inv_fact[n] = 1 * pow(fact[n], mod - 2, mod)

    for i in range(n - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1)
        inv_fact[i] %= mod

    return fact, inv_fact


def combination_mod(n, r, fact, inv_fact, mod):
    ans = 1
    ans *= fact[n]
    ans %= mod
    ans *= inv_fact[r]
    ans %= mod
    ans *= inv_fact[n - r]
    ans %= mod

    return ans


n, k = map(int, input().split())
mod = 10**9 + 7

fact, inv_fact = combination_init_mod(3000, mod)

for i in range(1, k + 1):
    if i == 1:
        print(n - k + 1)
    elif i - 1 <= n - k:
        ans = combination_mod(n - k + 1, i, fact, inv_fact, mod)
        ans %= mod
        ans *= combination_mod(k - 1, i - 1, fact, inv_fact, mod)
        ans %= mod
        print(ans)
    else:
        print(0)
