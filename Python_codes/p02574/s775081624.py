import math
n = int(input())
a = list(map(int, input().split()))

def prime_factorize(n):
  a = []
  while n % 2 == 0:
    a.append(2)
    n //= 2
  f = 3
  while f * f <= n:
    if n % f == 0:
      a.append(f)
      n //= f
    else:
      f += 2
  if n != 1:
    a.append(n)
  return a
r = [0] * (n+1)
sosu = [False for i in range(10**6+1)]

for i in range(n):
  r[i+1] = math.gcd(r[i],a[i])
if r[-1] != 1:
  print ('not coprime')
  exit()

for i in range(n):
  ary = set(prime_factorize(a[i]))
  for j in ary:
    if sosu[j]:
      print ('setwise coprime')
      exit()
    sosu[j] = True
print ('pairwise coprime')