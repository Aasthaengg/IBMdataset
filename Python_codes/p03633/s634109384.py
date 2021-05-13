from math import gcd
n=int(input())
a=int(input())
for _ in range(n-1):
  i=int(input())
  a=a*i//gcd(a,i)
print(a)