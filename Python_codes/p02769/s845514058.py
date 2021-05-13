N, K = list(map(int, input().split()))
p = 10**9+7
size = 2*2*10**5

def binom(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, size + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

res = 0

for i in range(min(K, N)+1):
        res += (binom(N, i, p) * binom(N-1, N-i-1, p)) % p

print(res % p)