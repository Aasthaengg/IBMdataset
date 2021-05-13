N,K = list(map(int,input().split()))
B = K
R = N-K

MAXN = 2000+5
p = 10**9+7
MOD = p
f = [1]
for i in range(MAXN):
    f.append(f[-1] * (i+1) % MOD)
def nCr(n, r, mod=MOD):
    return f[n] * pow(f[r], mod-2, mod) * pow(f[n-r], mod-2, mod) % mod

for i in range(1,K+1):
    if (i>R+1) or (i-1>B-1):
        print(0)
    else:
        X = nCr(R+1, i, mod=p)
        Y = nCr(B-1, i-1, mod=p)
        print(X*Y%p)