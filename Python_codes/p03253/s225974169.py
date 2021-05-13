n,m=map(int,input().split())
mod=10**9+7
N=2*10**5
fac=[1]*(N+3)
inv=[1]*(N+3)
t=1
for i in range(1,N+3):
    t*=i
    t%=mod
    fac[i]=t
t=pow(fac[N+2],mod-2,mod)
for i in range(N+2,0,-1):
    inv[i]=t
    t*=i
    t%=mod
def comb(n,r):
    if r>n or r<0:
        return 0
    return fac[n]*inv[n-r]*inv[r]%mod
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
import collections
c=collections.Counter(prime_factorize(m))
ans=1
for i,j in c.items():
    ans*=comb(n+j-1,j)
    ans%=mod
print(ans)