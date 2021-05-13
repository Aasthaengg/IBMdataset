def prime_factor(n):
    factors = {}
    if n % 2 == 0:
        cnt = 0
        while n % 2 == 0:
            cnt += 1
            n //= 2
        factors[2] = cnt
    i = 3
    while i * i <= n:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            factors[i] = cnt
        i += 2
    if n != 1:
        factors[n] = 1
    return factors

def combination(n, k, mod=10**9+7):
    numer = denom = 1
    for i in range(k):
        numer = numer * (n-i) % mod
        denom = denom * (i+1) % mod
    return numer * pow(denom, mod-2, mod) % mod

N, M = map(int, input().split())
mod = 10**9+7
ans = 1
for p, e in prime_factor(M).items():
    ans = ans * combination(e + N - 1, e) % mod
print(ans)