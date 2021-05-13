from collections import defaultdict
MOD=10**9+7
N=int(input())

def factorize(M):
  fact=defaultdict(int)
  for i in range(2,int(M**0.5)+1):
    if M==1:
      break
    while(M%i==0):
      M//=i
      fact[i]+=1
  
  if M!=1:
    fact[M]=1
  return fact

pdic=defaultdict(int)
for i in range(2,N+1):
  fact=factorize(i)
  for k,v in fact.items():
    pdic[k]+=v
#print(pdic)

answer=1
for v in pdic.values():
  answer*=(v+1)
  answer%=MOD
  
print(answer)