def ncr(n, r):
    return fac[n] * facinv[r] * facinv[n - r] % MOD


MOD = 10 ** 9 + 7
X, Y = map(int, input().split())

N = 10 ** 6
fac = [1, 1]
facinv = [1, 1]
inv = [0, 1]
for i in range(2, N + 1):
    fac.append(fac[i - 1] * i % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    facinv.append((facinv[-1] * inv[-1]) % MOD)

if (X + Y) % 3 or Y > 2 * X or Y < X // 2:
    print(0)
    exit()
d = (X + Y) // 3
print(ncr(d, X - (X + Y) // 3))
