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

sum=0
cnt_2=1
for i in range(len(L)):  
  if L[i] == "1":
    sum += cnt_2*powmod(3,len(L)-i-1)
    sum %= MOD
    cnt_2 = (cnt_2*2)%MOD
    
sum += cnt_2
sum %= MOD
print(sum)