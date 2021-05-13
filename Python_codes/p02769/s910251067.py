n,k=map(int,input().split())
mod=10**9+7
lim=n
fcl=[1]*(lim+1)
for i in range(1,lim+1):
  fcl[i]=(fcl[i-1]*i)%mod
def comb(x,y,p):
  return ((fcl[x]*pow(fcl[y],p-2,p))%p*pow(fcl[x-y],p-2,p))%p
ans=0
for i in range(min(n,k+1)):
  ans+=comb(n-1,n-i-1,mod)*comb(n,i,mod)
  ans%=mod
print(ans)