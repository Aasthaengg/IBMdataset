MOD=10**9+7
N,K=map(int,input().split())

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

term1=N-K+1
term2=1
for i in range(1,K+1):  
  #print(term1,term2)  
  print((term1*term2)%MOD)

  term1=term1*(N-K+1-i)*invmod(i+1)%MOD
  term2=term2*(K-i)*invmod(i)%MOD