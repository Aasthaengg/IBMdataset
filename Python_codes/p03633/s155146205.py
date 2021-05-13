from math import gcd

n=int(input())

lcm=0
for i in range(n):
  t=int(input())
  if lcm==0:
    lcm=t
  else:
    lcm=(t*lcm)//gcd(t,lcm)

print(lcm)