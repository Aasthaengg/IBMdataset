N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
mod = 10**9+7
ans = 0
fac = [1, 1] + [0]*(N-1)
finv = [1, 1] + [0]*(N-1)
inv = [1, 1] + [0]*(N-1)


def cmbInit():
    for i in range(2, N+1):
        fac[i] = fac[i-1]*i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i-1] * inv[i] % mod


def cmb(n, r):
    if n < r:
        return 0
    elif n < 0 or r < 0:
        return 0
    else:
        return fac[n] * (finv[r]*finv[n-r] % mod) % mod


cmbInit()

for i in range(N-1, K-2, -1):
    ans = (ans + (A[i]-A[N-1-i]) * cmb(i, K-1)) % mod

print(ans)
