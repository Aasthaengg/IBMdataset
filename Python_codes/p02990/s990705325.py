def mod_inverse(x, mod):
    return pow(x, mod - 2, mod)


# return nCk % mod
# it takes O(k)
def mod_comb(n, k, mod):
    numer, denom = 1, 1
    for i in range(k):
        numer = numer * ((n - i) % mod) % mod
        denom = denom * ((i + 1) % mod) % mod

    return numer * mod_inverse(denom, mod) % mod


mod = 10**9 + 7
N, K = map(int, input().split())

for i in range(1, K + 1):
    a = mod_comb(N - K + 1, i, mod)
    b = mod_comb(K - 1, i - 1, mod)
    print(a * b % mod)