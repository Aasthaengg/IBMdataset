a,b,c,d=map(int,input().split())

import math

def lcm(a,b):
  return (a*b)//math.gcd(a,b)

cnt_a=a-a//c-a//d+a//lcm(c,d)
cnt_b=b-b//c-b//d+b//lcm(c,d)

if a%c==0 or a%d==0:
  print(cnt_b-cnt_a)
else:
  print(cnt_b-cnt_a+1)