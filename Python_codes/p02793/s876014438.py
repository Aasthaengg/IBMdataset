def pow_r(x, n, P):
  if n == 0:
    return 1
  if n % 2 == 0:
    return pow_r(x ** 2 % P, n // 2, P)
  else:
    return x * pow_r(x ** 2 % P, n // 2, P) 

from fractions import gcd

N = int(input())
As = list(map(int, input().split()))
P = 10**9+7

if N == 1:
  print(1)
  exit()

lcm = As[0]*As[1]//gcd(As[0],As[1])
 
for i in range(2,N):
  c = gcd(lcm, As[i])
  lcm *= As[i]//c

rlt = 0
for a in As:
  rlt += lcm*pow_r(a, P-2, P) % P
  rlt %= P
print(rlt)