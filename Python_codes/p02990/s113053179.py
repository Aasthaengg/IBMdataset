N, K = map(int,input().split())
MOD = 10**9 + 7
fac = [1 for k in range(200010)]
inv = [1 for k in range(200010)]
finv = [1 for k in range(200010)]
for k in range(2,200010):
    fac[k] = (fac[k-1]*k)%MOD
    inv[k] = (MOD - inv[MOD%k] * (MOD // k))%MOD
    finv[k] = (finv[k - 1] * inv[k]) % MOD;
def nCr(n,r):
    return (fac[n]*finv[r]*finv[n-r])%MOD

for k in range(K):
    if k > N-K:
        print(0)
    else:
        print((nCr(K-1,k)*nCr(N-K+1,k+1))%MOD)
