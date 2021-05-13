import sys
from math import gcd
n,m=map(int,input().split())
s=input()
t=input()
l=gcd(n,m)
for i in range(l):
  if s[n//l*i]!=t[m//l*i]:
    print("-1")
    sys.exit()
print(n*m//l)