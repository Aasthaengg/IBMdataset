mod=998244353
n,m,k=map(int,input().split(' '))
F=[1 for i in range(n+1)]
for i in range(1,n+1):
    F[i]=F[i-1]*i%mod
I=[1 for i in range(n+1)]
for i in range(2,n+1):
    I[i]=(mod-int(mod/i))*I[mod%i]%mod
for i in range(2,n+1):
    I[i]=I[i]*I[i-1]%mod
def binom(n,k):
    return F[n]*I[k]%mod*I[n-k]%mod
pw=[1 for i in range(n+1)]
for i in range(1,n+1):
    pw[i]=pw[i-1]*(m-1)%mod
ans=0
for i in range(k+1):
    sz=n-i
    ans+=binom(n-1,i)*m%mod*pw[sz-1]%mod
    ans%=mod
print(ans)