from math import gcd
a, b, c, d = map(int, input().split())

t = b-a+1
b1 = b//c
b2 = b//d
if a%c==0:
  a1 = a//c - 1
else:
  a1 = a//c
if a%d==0:
  a2 = a//d - 1
else:
  a2 = a//d

lcm = c*d//gcd(c,d)
e1 = b//lcm
if a%(lcm)==0:
  e2 = a//(lcm) - 1
else:
  e2 = a//(lcm)
  
print(t-((b1-a1)+(b2-a2)-(e1-e2)))