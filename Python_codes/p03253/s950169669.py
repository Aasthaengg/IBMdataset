mod = 10**9+7
rng = 101001
fctr = [1]
finv = [1]
for i in range(1,rng):
  fctr.append(fctr[-1]*i%mod)
for i in range(1,rng):
  finv.append(pow(fctr[i],mod-2,mod))
def cmb(n,k):
  if n<0 or k<0:
    return 0
  else:
    return fctr[n]*finv[n-k]*finv[k]%mod
from collections import Counter
N,M = map(int,input().split())
if M == 1:
  print(1)
  exit()
pf = []
while M != 1:
  for i in range(2,int(M**0.5+1)):
    if M%i == 0:
      pf.append(i)
      M = M//i
      break
  else:
    pf.append(M)
    M = 1
cpf = list(Counter(pf).values())
ans = 1
for i in cpf:
  ans = (ans*cmb(N+i-1,i))%mod
print(ans)