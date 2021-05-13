n,k = map(int, input().split())

p = 10 ** 9 + 7
N = 10 ** 5 *5  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 3):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

ans = 0
if k < n:
    for i in range(k+1):
        ans += cmb(n,i,p)*cmb(n-1,n-i-1,p)
        ans %= p
else:
    for i in range(n):
        ans += cmb(n,i,p)*cmb(n-1,n-i-1,p)
        ans %= p

print(ans)
