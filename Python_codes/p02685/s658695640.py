n,m,k=map(int,input().split())
mod=998244353
res=0
pat=1
for i in range(0,k+1):
  res+=pat*pow(m-1,n-1-i,mod)
  pat*=(n-1-i)*pow(i+1,mod-2,mod)
  pat%=mod
  
print((m*res)%mod)