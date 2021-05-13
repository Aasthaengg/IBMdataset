N=int(input())
import math
def isprime(x):
  for i in range(2,math.floor(math.sqrt(x))+2):
    if x%i==0:
      return False
      break
  return True

               
L=[]
one=11
while len(L)<N:
  if isprime(one):
    L.append(one)
  one+=10
print(*L)  