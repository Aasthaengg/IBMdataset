import math
n = int(input())
a = list(map(int, input().split()))
f = 0
lcd = 1
for i in a:
  lcd = lcd * i // math.gcd(lcd, i)
for i in range(n):
  f +=  (lcd - 1) % a[i]
print(f)