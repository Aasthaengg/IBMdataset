MOD=1000000007
ans=0
N=int(input())
def modpow(a,x):
    ret=1
    while x>0:
        if x%2==1:
            ret*=a
            ret%=MOD
        a*=a
        x>>=1
    return ret

ans=modpow(10,N)+2*(MOD-modpow(9,N))+modpow(8,N)
print(ans%MOD)
