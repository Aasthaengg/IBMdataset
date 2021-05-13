from math import gcd
from collections import Counter
k=int(input())
t=[]
for a in range(1,k+1):
  for b in range(1,k+1):
    t.append(gcd(a,b))      
t=Counter(t)
ans=0
for d,e in t.items():
  for c in range(1,k+1):
    g=gcd(c,d)
    ans+=g*e
print(ans)
