from math import gcd

n=int(input())
t=[int(input()) for _ in range(n)]
lcm=t[0]
for i in range(1,n):
  lcm=(lcm*t[i])//gcd(lcm,t[i])
print(lcm)
