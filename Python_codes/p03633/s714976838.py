import math
def lcm(a,b):
  return (a*b)//math.gcd(a,b)
N=int(input())
s=1
for i in range(N):
  n=int(input())
  s=lcm(s,n)
print(s)