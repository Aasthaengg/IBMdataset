from math import gcd
N=int(input())
a,b,g=0,0,0
X=[]
zeroandzero=0
D=dict()
for i in range(N):
  a,b=map(int,input().split())
  if a==b==0:
    zeroandzero+=1
    N-=1
    continue
  g=gcd(a,b)
  a//=g
  b//=g
  if b<0:
    a,b=-a,-b
  D[(a,b)]=D.get((a,b),0)+1
E=dict()
K=list(D.keys())
mod=10**9+7
inv2=(mod+1)//2
P=pow(2,N,mod)
for i in range(len(K)):
  if E.get(K[i],0):
    continue
  g=list(K[i])
  if g[0]<0:
    g=(K[i][1],-K[i][0])
  else:
    g=(-K[i][1],K[i][0])
  E[g]=1
  g=(D[K[i]],D.get(g,0))
  if g[1]:
    P=P*pow(inv2,g[0]+g[1],mod)*(pow(2,g[0],mod)+pow(2,g[1],mod)-1)%mod
print((P-1+zeroandzero)%mod)