def inv(a,m=10**9+7):
    b=m
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return lastx % m

mod=10**9+7
n,k=map(int,input().split())
k=min(k,n-1)
frac=[1]
for i in range(1,n+1):
    frac.append(frac[-1]*i%mod)

ans=0
for i in range(k+1):
    tmp=inv(frac[i]**2%mod*frac[n-i]*frac[n-1-i]%mod)
    ans+=tmp
    ans%=mod
ans=ans*frac[n]*frac[n-1]%mod
print(ans)