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
frac=[1 for i in range(n+1)]
frac_inv=[1 for i in range(n+1)]
beki=[m for i in range(n+1)]

for i in range(1,n+1):
    frac[i]=frac[i-1]*i%mod
    frac_inv[i]=inv(frac[i],mod)
    beki[i]=beki[i-1]*(m-1)%mod
ans=0
for i in range(n-k,n+1):
    ans+=beki[i-1]*frac_inv[n-i]*frac_inv[i-1]%mod
    ans%=mod
print(ans*frac[n-1]%mod)