import sys
input=lambda: sys.stdin.readline().rstrip()
mod=10**9+7
n,m=map(int,input().split())
n_max=2*(10**5+1)
F,FI=[0]*(n_max+1),[0]*(n_max+1)
F[0],FI[0]=1,1
for i in range(n_max):
  F[i+1]=(F[i]*(i+1))%mod
FI[n_max-1]=pow(F[n_max-1],mod-2,mod)
for i in reversed(range(n_max-1)):
  FI[i]=(FI[i+1]*(i+1))%mod
def comb(x,y):
  return (F[x]*FI[x-y]*FI[y])%mod

pf={}
for i in range(2,int(m**0.5)+1):
  while m%i==0:
    pf[i]=pf.get(i,0)+1
    m//=i
if m>1:
  pf[m]=1

ans=1
for k in pf.keys():
  ans=(ans*comb(n-1+pf[k],pf[k]))%mod
print(ans)