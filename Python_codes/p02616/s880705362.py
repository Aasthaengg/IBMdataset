def resolve():
    n,k=map(int,input().split())
    a=sorted(list(map(int,input().split())))
    MOD=10**9+7
    ans=1
    if k==1:
        ans=a[-1]
    elif a[0]>=0 or (a[-1]<0 and k%2==1):
        for i in a[-k:]:
            ans=(ans*i)%MOD
    elif a[-1]<0 and k%2==0:
        for i in a[:k]:
            ans=(ans*i)%MOD
    else:
        ans=1
        if k%2==1 and n>=3:
            ans*=a[-1]
            ans%=MOD
            l,r=0,-2
            lm=a[0]*a[1]
            rm=a[-2]*a[-3]    
        else:
            l,r=0,-1
            lm=a[0]*a[1]
            rm=a[-1]*a[-2]
        for i in range(k//2):
            if lm>=rm:
                ans*=lm%MOD
                l+=2
                if l<=n-2:
                    lm=a[l]*a[l+1]
            else:
                ans*=rm%MOD
                r-=2
                if 1<=n+r:
                    rm=a[r]*a[r-1]
            ans%=MOD
    print(ans)

if __name__ == '__main__':
    resolve()