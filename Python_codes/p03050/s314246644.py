from math import ceil
n = int(input())

total = 0
for i in range(ceil(n ** 0.5) + 1):
  if n % (i + 1) == 0:
    a = n // (i + 1) - 1
    if a >= 2 and n // a == n % a:
      total += a

print(total)