x,y=map(int,input().split())
mod=10**9+7

def modpow(a,n):
    if n<1:
        return 1
    ans=modpow(a,n//2)
    ans=(ans*ans)%mod
    if n%2==1:
        ans*=a
    return ans%mod
    
def conb(n,i):
    inv,ans=1,1
    for j in range(1,i+1):
        ans=ans*(n-j+1)%mod
        inv=inv*j%mod
    return (ans*modpow(inv,mod-2))%mod


if (x+y)%3!=0:
    print(0)
else:
    n=(x+y)//3
    x=x-n
    y=y-n
    if x<0 or y<0:
        print(0)
    else:
        ans=conb(x+y,x)
        print(ans)
