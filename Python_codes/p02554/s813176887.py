N=int(input())
MOD=10**9+7
MAX=N+1
def powermod(base,ind):
  if ind==1:
    return base
  elif ind%2==0:
    return (powermod(base,ind//2)**2)%MOD
  else:
    return ((powermod(base,ind//2)**2)*base)%MOD

print((powermod(10,N)-2*powermod(9,N)+powermod(8,N))%MOD)