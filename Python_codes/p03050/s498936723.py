n = int(input())
from math import gcd
cou = 0
for i in range(1,int(n**0.5)+1):
  if n%i==0:
    b = n//i-1
    if b>=2 and n//b==n%b:
      cou += b
    
    if i>2:
      c = i-1
      if n//c==n%c:
        cou += c
print(cou)