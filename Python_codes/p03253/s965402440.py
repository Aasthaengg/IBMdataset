n, m = map(int, input().split())

if m == 1:
    print(1)
    exit()

mod = 10**9+7

import math
def factorize(n):
    d = {}
    temp = int(math.sqrt(n))+1
    for i in range(2, temp):
        while n%i== 0:
            n //= i
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    if d == {}:
        d[n] = 1
    else:
        if n in d:
            d[n] += 1
        elif n != 1:
            d[n] =1
    return d

mod = 10**9+7
N = 10**6
fac = [1]*(N+1)
finv = [1]*(N+1)
for i in range(N):
    fac[i+1] = fac[i] * (i+1) % mod
finv[-1] = pow(fac[-1], mod-2, mod)

for i in reversed(range(N)):
    finv[i] = finv[i+1] * (i+1) % mod

def cmb1(n, r, mod):
    if r <0 or r > n:
        return 0
    r = min(r, n-r)
    return fac[n] * finv[r] * finv[n-r] % mod

d = factorize(m)
ans = 1
for k, v in d.items():
    ans *= cmb1(v+n-1, n-1, mod)
    ans %= mod
print(ans)
