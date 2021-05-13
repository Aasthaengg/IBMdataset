max_n=10**6
mod=10**9+7

frac=[1]
for i in range(1,max_n+1):
  frac.append((frac[-1]*i)%mod)

inv=[1,1]
inv_frac=[1,1]
for i in range(2,max_n):
  inv.append((mod-inv[mod%i]*(mod//i))%mod)
  inv_frac.append((inv_frac[-1]*inv[-1])%mod)
  
def perm(m,n):
  if m<n:
    return 0
  if m==1:
    return 1
  return (frac[m]*inv_frac[m-n])%mod

def comb(m,n):
  if m<n:
    return 0
  if m==1:
    return 1
  return (frac[m]*inv_frac[n]*inv_frac[m-n])%mod




n,m=map(int,input().split())
l=[]
for i in range(2,int(m**0.5)+1):
  if m%i==0:
    c=0
    while m%i==0:
      m//=i
      c+=1
    l.append(c)
if m!=1:
  l.append(1)

r=1
for i in l:
  r=(r*comb(n+i-1,i))%mod
print(r)