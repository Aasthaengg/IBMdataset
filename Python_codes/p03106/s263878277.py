a,s,d=map(int,input().split())
from fractions import gcd
f=gcd(a,s)
for i in range(f,0,-1):
  if f%i:continue
  d-=1
  if d:continue
  print(i);exit()