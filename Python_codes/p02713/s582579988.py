from math import gcd
from functools import reduce

def gcd_list(lis):
  return reduce(gcd, lis)

K = int(input())

ans = 0
for i in range(1,K+1):
  for j in range(1,K+1):
    for k in range(1,K+1):
      ans += gcd_list([i,j,k])
      
print(ans)