n, p = map(int, input().split())
arr = list(map(int, input().split()))

a = sum([x % 2 == 1 for x in arr])
b = n - a


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p


MOD = 10**18 + 7
N = 10**6
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

start = p

# aから奇数個 or 偶数個選ぶ
ans = 0
for i in range(p, a + 1, 2):
    for j in range(b + 1):
        ans += cmb(a, i, MOD) * cmb(b, j, MOD)

print(ans)