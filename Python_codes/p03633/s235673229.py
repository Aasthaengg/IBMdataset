import math
def lcm(a, b):
  return abs(a*b) // math.gcd(a, b)
n=int(input())
t=int(input())
for i in range(n-1):
  t=lcm(t,int(input()))
print(t)