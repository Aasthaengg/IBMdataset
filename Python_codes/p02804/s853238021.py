n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

mod=10**9+7
fcl=[1]*(n+1)
for i in range(1,n+1):
  fcl[i]=(fcl[i-1]*i)%mod
def comb(x,y,p):
  return ((fcl[x]*pow(fcl[y],p-2,p))%mod*pow(fcl[x-y],p-2,p))%mod

maxs=0
for i in range(k,n+1):
  maxs+=a[i-1]*comb(i-1,k-1,mod)
  maxs%=mod
mins=0
for i in range(n-k+1):
  mins+=a[i]*comb(n-i-1,k-1,mod)
  mins%=mod
ans=(maxs-mins)%mod
print(ans+mod if ans<0 else ans)