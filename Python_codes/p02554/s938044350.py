def main():
    mod=1000000007
    n=int(input())
    if n==1:
        return 0
    
    inv=lambda x: pow(x,mod-2,mod)
    Fact=[1] #階乗
    for i in range(1,n+1):
        Fact.append(Fact[i-1]*i%mod)
    Finv=[0]*(n+1) #階乗の逆元
    Finv[-1]=inv(Fact[-1])
    for i in range(n-1,-1,-1):
        Finv[i]=Finv[i+1]*(i+1)%mod
    def comb(n,r):
        if n<r:
            return 0
        return Fact[n]*Finv[r]*Finv[n-r]%mod

    ans=0
    p=2**2
    others=pow(8,n-2,mod)
    for i in range(2,n+1):
        c=comb(n,i)
        ans+=(p-2)*others*c
        ans%=mod
        p*=2
        p%=mod
        others*=inv(8)
        others%=mod
    return ans

if __name__=='__main__':
    print(main())