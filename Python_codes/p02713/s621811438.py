from math import gcd

def gcd3(a, b, c):
  return gcd(gcd(a, b), c)

K = int(input())

res = 0
for a in range(1, K+1):
  for b in range(1, K+1):
    for c in range(1, K+1):
      res += gcd3(a, b, c)
      
print(res)