from math import gcd
a,b,c,d=map(int,input().split())
def lcm(x,y):return x*y//gcd(x,y)
def f(x):
  return x-x//c-x//d+x//lcm(c,d)
print(f(b)-f(a-1))