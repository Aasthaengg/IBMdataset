def inv(a,m):
    b=m
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return lastx % m

mod=998244353
n,m,k=map(int,input().split())
frac=[1];frac_inv=[1]
beki=m
ans=0

for i in range(1,n+1):
    frac.append(frac[-1]*i%mod)
    frac_inv.append(inv(frac[-1],mod))

for i in range(n-k-1):
    beki=beki*(m-1)%mod
for i in range(n-k,n+1):
    ans+=beki*frac[n-1]*frac_inv[n-i]*frac_inv[i-1]%mod
    beki=beki*(m-1)%mod
print(ans%mod)