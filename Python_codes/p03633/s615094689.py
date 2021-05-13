import fractions

N = int(input())
a = int(input())

for _ in range(N-1):
  b = int(input())
  c = fractions.gcd(a,b)
  d = a // c
  e = b // c
  a = d*e*c
  
print(a)