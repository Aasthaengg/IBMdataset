n,k = map(int,input().split())
mod = 10**9+7
def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

fac = [0]*(n+1)
fac[0] = 1
fac[1] = 1
for i in range(2,n+1):
    fac[i] = fac[i-1] * i % mod

def combi(n,r,mod=10**9+7):
    return( ( fac[n] * modinv(fac[r]) )%mod * modinv(fac[n-r]) % mod)

ans = 0
for i in range(min(k+1,n)):
    ans += combi(n,i)*combi(n-1,n-i-1) % mod
    ans %= mod
print(ans % mod)