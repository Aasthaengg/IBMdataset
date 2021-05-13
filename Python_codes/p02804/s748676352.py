N,K = list(map(int,input().split()))
A = list(map(int,input().split()))

A.sort()

MAXN = 10**5+10
p = 10**9+7
MOD = p
f = [1]
for i in range(MAXN):
    f.append(f[-1] * (i+1) % MOD)
def nCr(n, r, mod=MOD):
    return f[n] * pow(f[r], mod-2, mod) * pow(f[n-r], mod-2, mod) % mod

MA = 0
for i in range(N-K+1):
    MA = (MA + A[N-1-i]*nCr(N-1-i,K-1))%p

MI = 0
for i in range(N-K+1):
    MI = (MI + A[i]*nCr(N-1-i,K-1))%p

out = MA-MI
if out<0:
    out += p
print(out)