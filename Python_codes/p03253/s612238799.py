import math
import sys

def findFactors(n):
    now=n
    f=[]
    while now%2==0:
        now//=2
        f.append(2)
    p=3
    while p<=math.sqrt(n):
        while now%p==0:
            now//=p
            f.append(p)
        p+=2
        if now==1:
            break
    if now>math.sqrt(n):
        f.append(now)
    return f

def cmb(n,r):
    if (r<0 or r>n):
        return 0
    r=min(r,n-r)
    return g1[n]*g2[r]*g2[n-r]%mod

mod=10**9+7
N=10**5+100
g1=[1,1]
g2=[1,1]
inverse=[0,1]

#n!とその逆元を求めておく
for i in range(2,N+1):
    g1.append((g1[-1]*i)%mod)
    inverse.append((-inverse[mod%i]*(mod//i))%mod)
    g2.append((g2[-1]*inverse[-1])%mod)

n,m=map(int,input().split())
if m==1:
    print(1)
    sys.exit()

F=findFactors(m)
ans=1

now=F[0]
cnt=0
for f in F:
    if f==now:
        cnt+=1
    else:
        ans*=cmb(n-1+cnt,cnt)
        ans%=mod
        now=f
        cnt=1
ans*=cmb(n-1+cnt,cnt)
ans%=mod
print(ans)