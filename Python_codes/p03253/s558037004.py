def factors(n):
    f = []
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    if c > 0:
        f.append([2, c])
    p = 3
    while p * p <= n:
        if n % p == 0:
            c = 0
            while n % p == 0:
                n //= p
                c += 1
            if c > 0:
                f.append([p, c])
        p += 2
    if n != 1:
        f.append([n, 1])
    return f

MOD = 1000000007
N, M = map(int, input().split())

fact = [0] * (N+35)
finv = [0] * len(fact)
inv  = [0] * len(fact)

fact[0] = fact[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1
for i in range(2, len(fact)):
    fact[i] = fact[i-1] * i % MOD
    inv[i] = - inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD

nCr = lambda n, r: fact[n] * finv[n-r] * finv[r] % MOD

ans = 1

for _, x in factors(M):
    ans = ans * nCr(x+N-1, x) % MOD

print(ans)