def main():
    n,k=map(int,input().split())
    MOD=10**9+7

    def pre(n,MOD):
        a=1
        for i in range(1,n+1):
            a=(a*i)%MOD
        an=a
        b=pow(a,MOD-2,MOD)
        bs=[1]*(n+1)
        bs[n]=b
        for i in range(n,1,-1):
            b=b*i%MOD
            bs[i-1]=b
        return an,bs

    a,b=pre(n-1,MOD)
    ans=1
    for i in range(1,min(n-1,k)+1):
        s=(a*n*b[i])%MOD
        s=(s*b[n-i])%MOD
        s=(s*a*b[n-i-1])%MOD
        s=(s*b[i])%MOD
        ans+=s
        ans%=MOD
    print(ans)
    
if __name__ == '__main__':
    main()