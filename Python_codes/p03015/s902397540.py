MOD=10**9+7
L=input()

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
    
sum=0
cnt_2=1
pow_3=powmod(3,len(L))
inv_3=invmod(3)
for i in range(len(L)):
  pow_3=pow_3*inv_3%MOD
  if L[i] == "1":
    sum += cnt_2*pow_3
    sum %= MOD
    cnt_2 = (cnt_2*2)%MOD
    
sum += cnt_2
sum %= MOD
print(sum)