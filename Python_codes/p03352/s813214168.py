n = int(input())
import math as m
if n < 4:
  print(1)
  exit(0)
  
perfect = 1
for b in range(2,int(n**0.5)+1):
  p = int(m.log(n,b))
  x = b**(p+1)
  if x > n:
    x = b**p
  perfect = max(perfect,x)
  #print(b,x)
  if perfect == n:
    break

print(perfect)
