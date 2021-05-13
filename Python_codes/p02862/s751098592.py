x,y=map(int,input().split())
if (x+y)%3:print(0)
else:
    sab=(x+y)//3
    a=y-sab
    b=sab-a
    if a<0 or b<0:print(0);exit()
    mod=10**9+7
    fact=[1]*(sab+1)
    inv=[1]*(sab+1)
    for i in range(2,sab+1):
        fact[i]=i*fact[i-1]%mod
    inv[-1]=pow(fact[-1],mod-2,mod)
    for i in range(sab,1,-1):
        inv[i-1]=inv[i]*i%mod
    def comb(x,y):return fact[x]*inv[y]%mod*inv[x-y]%mod if x>=y>=0 else 0
    print(comb(sab,a))