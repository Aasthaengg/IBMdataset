import math
n = int(input())
a = int(input())
for i in range(n - 1):
  b = int(input())
  a = a * b // math.gcd(a, b)
print(a)