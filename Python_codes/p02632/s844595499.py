K=int(input())
S=input()
N=len(S)
mod=10**9+7

def cmb(n,r):
  global mod
  if r<0 or r>n:
    return 0
  return (g1[n]*g2[r]*g2[n-r])%mod

g1=[1,1]
g2=[1,1]
inv=[0,1]
for i in range(2,3000003):
  g1.append((g1[-1]*i)%mod)
  inv.append((-inv[mod%i]*(mod//i))%mod)
  g2.append((g2[-1]*inv[-1])%mod)
P=0
for i in range(K+1):
  P+=pow(26,i,mod)*pow(25,K-i,mod)*cmb(N+K-i-1,K-i)
print(P%mod)