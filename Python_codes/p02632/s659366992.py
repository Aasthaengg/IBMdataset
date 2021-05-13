K = int(input())
S = input()
L = len(S)
MOD = 10**9+7

MAXN = K+L+5
fac = [1,1] + [0]*MAXN
finv = [1,1] + [0]*MAXN
inv = [0,1] + [0]*MAXN
for i in range(2,MAXN+2):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = -inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i-1] * inv[i] % MOD

def comb(n,r):
    if n < r: return 0
    if n < 0 or r < 0: return 0
    return fac[n] * (finv[r] * finv[n-r] % MOD) % MOD

ans = 0
for i in range(K+1):
    ans += comb(L-1+i,i) * pow(25,i,MOD) * pow(26,K-i,MOD)
    ans %= MOD
print(ans)