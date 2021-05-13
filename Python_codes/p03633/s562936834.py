from math import gcd
def lcm(a,b):
  return a*b//gcd(a,b)
N=int(input())
T=[0]*N
for i in range(N):
  T[i]=int(input())
ans=1
for i in range(N):
  ans=lcm(ans,T[i])
print(ans)