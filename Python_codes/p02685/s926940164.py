mod=998244353
def mod_pow(x,n):
    res=1
    while n>0:
        if n&1:
            res=res*x%mod
        x=x*x%mod
        n>>=1
    return res
def inverse_element(t):
    return mod_pow(t,mod-2)

n,m,k=map(int,input().split())
if m==1:
    if k==n-1:
        print(m)
    else:
        print(0)
    exit(0)
ans=0
p1=m*mod_pow(m-1,n-1)%mod
p2=1
for i in range(0,k+1):
    ans+=p1*p2%mod
    ans%=mod
    p1*=inverse_element(m-1)
    p2*=(n-i-1)
    p2*=inverse_element(i+1)
    p1%=mod
    p2%=mod
print(ans%mod)