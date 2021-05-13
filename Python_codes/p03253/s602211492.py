n,m=map(int,input().split())

def prime_factorize(n):
    n_origin=n+0
    primelist=[]
    a=2
    while a*a<=n_origin:
        if n%a!=0:
            a+=1
            continue
        ex=0
        while n%a==0:
            ex+=1
            n=n//a
        primelist.append([a,ex])
        a+=1
    if n!=1:
        primelist.append([n,1])
    return primelist

#nCkをmodで割ったあまり
#テーブルを作る前処理
mod=10**9+7
fac=[0,1]
finv=[0,1]
inv=[0,1]
nmax=110000
for i in range(2,nmax+1):
    fac.append(fac[i-1]*i%mod)
    inv.append(mod-inv[mod%i]*(mod//i)%mod)
    finv.append(finv[i-1]*inv[i]%mod)
#二項係数計算部分
def combinations_mod(n,k,mod):
    if n<k:
        return 0
    if n<0 or k<0 :
        return 0
    if k==0 :
        return 1
    return fac[n]*(finv[k]*finv[n-k]%mod)%mod
primelist=prime_factorize(m)
ans=1
for pi,bi in primelist:
    ans=(ans*combinations_mod(bi+n-1,n-1,mod))%mod
print(ans)
