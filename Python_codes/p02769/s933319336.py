n,k=map(int,input().split())
mod=10**9+7

#n!とその逆元を求めておく
N=4*10**5+10
g1=[1,1] #n!
g2=[1,1] #n!の逆元
inverse=[0,1]
for i in range(2,N+1):
    g1.append((g1[-1]*i)%mod)
    inverse.append((-inverse[mod%i]*(mod//i))%mod)
    g2.append((g2[-1]*inverse[-1])%mod)

def cmb(n,r): #nCrを求める
    if (r<0 or r>n):
        return 0
    r=min(r,n-r)
    return g1[n]*g2[r]*g2[n-r]%mod

if n<=k-1:
    print(cmb(2*n-1,n))
else:
    ans=0
    for a in range(k+1):
        ans+=cmb(n,a)*cmb(n-1,a)%mod
        ans%=mod
    print(ans)