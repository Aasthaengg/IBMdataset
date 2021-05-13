n,k=map(int,input().split())
l=list(map(int,input().split()))
N=n
mod=10**9+7
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
import collections
c=collections.Counter(l)
l=list(c.items())
l.sort()
ans=0
t=0
for i,j in l:
    t+=j
    if t<k:
        continue
    for x in range(1,j+1):
        ans+=i*comb(j,x)*comb(t-j,k-x)
        ans%=mod
t=0
for i,j in l[::-1]:
    t+=j
    if t<k:
        continue
    for x in range(1,j+1):
        ans-=i*comb(j,x)*comb(t-j,k-x)
        ans%=mod
print(ans)