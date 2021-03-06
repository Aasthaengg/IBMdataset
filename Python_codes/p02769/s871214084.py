n,k = map(int,input().split())

mod = 10**9 + 7
l = 10**7
fac = [1]*l
facr = [1]*l

for i in range(l-1):
    fac[i+1] = fac[i]*(i+1)%mod
facr[l-1] = pow(fac[l-1],mod - 2,mod)
for i in range(1,l)[::-1]:
    facr[i-1] = facr[i]*i%mod

def combi(N,K):
    return fac[N]*facr[N-K]%mod*facr[K]%mod

ans = 1
for i in range(1,min(n,k+1)):
    ans += combi(n,i)*combi(n-1,i)%mod
    ans %= mod
print(ans)
