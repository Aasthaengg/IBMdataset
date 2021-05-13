import math
a,b,c,d=map(int, input().split())
def f(x,y,z):
  return x//y+x//z-x*math.gcd(z,y)//(y*z)
print(b-a+1-f(b,c,d)+f(a-1,c,d))