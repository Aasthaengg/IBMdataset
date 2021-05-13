MOD=10**9+7
def powmod(a,p):
  if p==0:
    return 1
  elif p==1:
    return a
  else:
    pow2=powmod(a,p//2)
    if p%2==0:
      return (pow2**2)%MOD
    else:
      return (a*pow2**2)%MOD
def invmod(a):
  return powmod(a,MOD-2)
def comb_mod(n,r):
  nPr=1
  fact_r=1
  for i in range(r):
    nPr*=n-i
    nPr%=MOD
    fact_r*=r-i
    fact_r%=MOD  
  return (nPr*invmod(fact_r))%MOD

N,K=map(int,input().split())

for i in range(1,K+1):
  term1=comb_mod(N-K+1,i)
  term2=comb_mod(K-1,K-i)
  print(term1*term2%MOD)