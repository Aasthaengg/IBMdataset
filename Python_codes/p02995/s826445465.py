import math

a,b,c,d = map(int,input().split())

l = c*d//math.gcd(c,d)

def cnt(x):
  return b//x - a//x + int(a%x==0)

print(b-a+1 - cnt(c) - cnt(d) + cnt(l))