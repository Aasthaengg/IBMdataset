def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


N, K = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
p = 10 ** 9 + 7
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

i = 0
f_max = 0
f_min = 0
while N - 1 - i >= K - 1:
    r = cmb(N - 1 - i, K - 1, p)
    f_max += a[i] * r
    f_min += a[N - i - 1] * r
    i += 1

print((f_max - f_min) % p)

