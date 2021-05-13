nmax = 10**5+1
mod = 10**9+7

fac = [1]*nmax
finv = [1]*nmax
inv = [1]*nmax
def ncr_pre():
    for i in range(2,nmax):
        fac[i] = fac[i-1]*i % mod
        inv[i] = mod - inv[mod%i] * (mod//i) %mod
        finv[i] = finv[i-1] * inv[i] %mod

def ncr(n,r):
    if n<r:
        return 0
    if n<0 or r<0:
        return 0
    return fac[n]* (finv[r] * finv[n-r] %mod) %mod


import collections
ncr_pre()
n,k = map(int,input().split())
A = list(map(int,input().split()))
co = sorted(collections.Counter(A).items())
smax = 0
c= 0
l = len(co)
for i in range(l):
    num,cnt = co[i]
    c+=cnt
    if c>=k:
        smax += num*(ncr(c,k) - ncr(c-cnt,k))
        smax%=mod
smin = 0
c= 0
for i in range(l):
    num,cnt = co[-i-1]
    c+=cnt
    if c>=k:
        smin += num*(ncr(c,k) - ncr(c-cnt,k))
        smin%=mod
print((smax - smin)%mod)
