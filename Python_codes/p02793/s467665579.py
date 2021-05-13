N = int(input())
A = list(map(int,input().split()))
mod = 10**9+7

import fractions
from functools import reduce

def gcd(x,y):
  if x == 0:
    return y
  else:
    return gcd(y-x*(y//x),x)
 

def lcm(x, y):
    return (x*y)//gcd(x,y)
    
l = 1
B = 0

for i in range(N):
  l = lcm(l,A[i])
for i in range(N):
  B += l//A[i]
B %= mod

print(B)