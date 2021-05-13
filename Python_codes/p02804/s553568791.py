N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 10**9+7
def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

fac = [0]*(N+1)
fac[0] = 1
fac[1] = 1
for i in range(2,N+1):
    fac[i] = fac[i-1] * i % mod

def combi(n,r,mod=10**9+7):
    return( ( fac[n] * modinv(fac[r]) )%mod * modinv(fac[n-r]) % mod)

A.sort()
ans = 0
for i in range(1, N-K+2):
    ans += combi(N-i, K-1)*A[N-i] % mod
    ans += mod
    ans -= combi(N-i, K-1)*A[i-1] % mod

print(ans%mod)