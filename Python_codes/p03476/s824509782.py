import math
from itertools import accumulate
q=int(input())
l=[]
r=[]
for i in range(q):
  a,b=list(map(int,input().split()))
  l.append(a)
  r.append(b)
  
def is_prime(n):
  if n==1:
    return False
  elif n==2:
    return True
  else:
    for i in range(2,int(math.sqrt(n)+1)):
      if n%i==0:
        return False
  return True

l_min=min(l)
r_max=max(r)
ruiseki=[]
for i in range(l_min,r_max+1):
  if i%2==1 and is_prime(i) and is_prime((i+1)//2):
    ruiseki.append(1)
  else:
    ruiseki.append(0)
    
ruiseki=[0]+list(accumulate(ruiseki))

for i in range(q):
  print(ruiseki[r[i]-l_min+1]-ruiseki[l[i]-l_min])
  
    
    
  
