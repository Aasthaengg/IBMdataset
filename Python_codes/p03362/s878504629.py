import math
N=int(input())

def isPrime(n):
  for k in range(2,int(math.sqrt(n))+2):
    if n%k==0:
      return False
  else:
    return True

plist=[2]
p=11
while(len(plist)<N):
  if p%5==1 and isPrime(p):
    plist.append(p)
  p+=10
    
print(" ".join(map(str,plist)))