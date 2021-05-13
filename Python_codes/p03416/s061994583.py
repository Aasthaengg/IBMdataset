import numpy as np


def split_digits(n):
  digits = []
  while n > 0:
    digits.append(n % 10)
    n = int(n / 10)
  return digits


a, b = map(int, input().split())
c = 0

for i in range(a, b + 1):
  digits = np.array(split_digits(i))
  if (digits == digits[::-1]).all():
    c += 1
    
print(c)
