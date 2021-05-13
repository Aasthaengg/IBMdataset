
#かけて最小公倍数になる　そのために必要な数がB
from fractions import gcd
N=int(input())
if N==1:
  print(1)
  exit()

mod=10**9+7
A=list(map(int, input().split()))
def lcm(a,b):
  return a//gcd(a,b)*b

if N==2:
  LCM=lcm(A[0],A[1])
  ans=((LCM//A[0])+(LCM//A[1]))%mod
  print(ans)
  exit()

LCM=1
#LCM%=mod
for a in A:
  LCM=lcm(LCM, a)
  #LCM%=mod
  
#print(LCM)
ans=0
for a in A:
  ans+=LCM//a
  #ans%=mod

print(int(ans%mod))

