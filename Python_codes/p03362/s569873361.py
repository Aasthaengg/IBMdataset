import math
N=int(input())

def isPrime(n):
  for k in range(2,int(math.sqrt(n))+2):
    if n%k==0:
      return False
  else:
    return True

plist=[]
p=1
while(len(plist)<N):
  p+=10
  if isPrime(p):
    plist.append(p)
    
print(*plist)