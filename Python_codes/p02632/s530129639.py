import sys
input=lambda: sys.stdin.readline().rstrip()
k=int(input())
S=input()
mod=10**9+7
n=len(S)
n_max=2*(10**6+1)
F,FI=[0]*(n_max+1),[0]*(n_max+1)
F[0],FI[0]=1,1
for i in range(n_max):
  F[i+1]=(F[i]*(i+1))%mod
FI[n_max-1]=pow(F[n_max-1],mod-2,mod)
for i in reversed(range(n_max-1)):
  FI[i]=(FI[i+1]*(i+1))%mod
def comb(x,y):
  return (F[x]*FI[x-y]*FI[y])%mod

P1,P2=[1],[1]
for _ in range(10**6):
  P1.append((P1[-1]*26)%mod)
  P2.append((P2[-1]*25)%mod)

ans=0
for i in range(n,n+k+1):
  ans+=comb(i-1,n-1)*P2[i-n]*P1[n+k-i]
  ans%=mod
print(ans)
