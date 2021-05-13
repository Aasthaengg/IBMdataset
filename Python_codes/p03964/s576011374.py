n = int(input())

#a,bの最大公約数
def gcd(a, b):
   while b:
       a, b = b, a % b
   return a

#a,bの最小公倍数
def lcm(a, b):
   return a * b // gcd (a, b)

def ceil(a, b):
  return a // b + (a % b > 0)

import math
ans = (1, 1)
for _ in range(n):
   t,a = map(int,input().split())
   b = max(ceil(ans[0],t), ceil(ans[1],a))
   ans = [b*t, b*a]
print(sum(ans))
   

