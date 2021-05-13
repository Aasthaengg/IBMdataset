import math

L,R=map(int, input().split())
d=R-L
r=R%2019
l=L%2019

if d>=2019 or r<l:
  print(0)
  
else:
  k=2020
  for i in range(l,r+1):
    for j in range(i+1,r+1):
      k=min(k,i*j%2019)
  print(k)

