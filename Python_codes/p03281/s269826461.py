import math
from collections import Counter
n=int(input())



def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)

    return a
ans=0
for i in range(1,n+1):
  if i%2==0:
    continue
  s=Counter(prime_factorize(i))
  cnt=1
  for j in s.values():
    cnt*=j+1
    
    
  if cnt==8:
    ans+=1
    #print(s)
  else:
    continue
    
print(ans)