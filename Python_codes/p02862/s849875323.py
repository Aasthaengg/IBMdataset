x,y=map(int,input().split())
if not((2*x-y)%3==0 and (-x+2*y)%3==0):
  print(0)
  exit()
p=(2*x-y)//3
q=(-x+2*y)//3

def cmb(n,r,mod):
  if r<0 or n<r:
    return 0
  r=min(r,n-r)
  return g1[n]*g2[r]*g2[n-r]%mod
n=p+q
mod=10**9+7
g1=[1,1]#元table
g2=[1,1]#逆元table
inv=[0,1]#逆元table計算用
for i in range(2,n+1):
  g1.append(g1[-1]*i%mod)
  inv.append(-inv[mod%i]*(mod//i)%mod)
  g2.append(g2[-1]*inv[-1]%mod)

print(cmb(n,p,mod))