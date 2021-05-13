def nck(n, k):
    numer, denom = 1, 1
    for i in range(k):
        numer = numer * (n-i) % MOD
        denom = denom * (k-i) % MOD
    return numer * pow(denom, MOD-2, MOD) % MOD

x, y = map(int, input().split())
MOD = 10 ** 9 + 7

i = 2 * y - x
j = 2 * x - y
if i % 3 != 0 or j % 3 != 0 or i < 0 or j < 0:
    print(0)
else:
    i, j = i // 3, j // 3
    print(nck(i+j, min(i, j)))
