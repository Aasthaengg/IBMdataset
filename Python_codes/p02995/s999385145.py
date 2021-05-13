import math

a,b,c,d=map(int, input().split())

lcm=c*d//math.gcd(c,d)

ac=a//c
ad=a//d
acd=a//lcm
bc=b//c
bd=b//d
bcd=b//lcm

A=a-ac-ad+acd
B=b-bc-bd+bcd

if a%c==0 or a%d==0:
  print(B-A)
else:
  print(B-A+1)