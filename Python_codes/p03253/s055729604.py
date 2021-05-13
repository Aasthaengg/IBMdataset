n,m = map(int,input().split())
mod = 10**9 + 7
l = n+1000
fac = [1]*l
facr = [1]*l

for i in range(l-1):
    fac[i+1] = fac[i]*(i+1)%mod
facr[l-1] = pow(fac[l-1],mod - 2,mod)
for i in range(1,l)[::-1]:
    facr[i-1] = facr[i]*i%mod

def combi(N,K):
    return fac[N]*facr[N-K]%mod*facr[K]%mod

prime = {}
i = 2
x = m
while i*i <= m:
    if x%i == 0:
        prime[i] = 0
        while x%i == 0:
            x = x//i
            prime[i] += 1
    i += 1
if x > 1:
    prime[x] = 1
ans = 1
for q in prime.values():
    ans *= combi(q+n-1,n-1)
    ans %= mod
print(ans)
