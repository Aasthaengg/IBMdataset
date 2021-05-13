n, k = map(int, input().split())

mod = 10 ** 9 + 7

fac = [1, 1]
finv = [1, 1]
inv = [0, 1]
for i in range(2, n+1):
    fac.append(fac[-1] * i % mod)
    inv.append(-inv[mod%i] * (mod // i) % mod)
    finv.append(finv[-1] * inv[-1] % mod)

ans = 0
for i in range(min(n-1, k) + 1):
    com1 = fac[n] * finv[i] * finv[n-i] % mod
    com2 = fac[n-1] * finv[i] * finv[n-i-1] % mod
    mul = com1 * com2 % mod
    ans = (ans + mul) % mod

print(ans)