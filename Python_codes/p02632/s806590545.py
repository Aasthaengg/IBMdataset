import sys
readline = sys.stdin.readline

MOD = 10**9+7
def frac(limit):
    frac = [1]*limit
    for i in range(2,limit):
        frac[i] = i * frac[i-1]%MOD
    fraci = [None]*limit
    fraci[-1] = pow(frac[-1], MOD -2, MOD)
    for i in range(-2, -limit-1, -1):
        fraci[i] = fraci[i+1] * (limit + i + 1) % MOD
    return frac, fraci
frac, fraci = frac(2341398)
def comb(a, b):
    if not a >= b >= 0:
        return 0
    return frac[a]*fraci[b]*fraci[a-b]%MOD

K = int(readline())
S = len(readline().strip())
ans = 0

M = 1341398
A = [1]*M
B = [1]*M
for i in range(1, M):
    A[i] = (A[i-1]*25)%MOD
    B[i] = (B[i-1]*26)%MOD

ans = 0

for i in range(K+1):
    ans = (ans+A[i]*B[K-i]*comb(i+S-1, i))%MOD

print(ans)

