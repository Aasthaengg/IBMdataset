import numpy as np


def sum_of_digits(x):
  res = np.zeros_like(x)
  for i in range(len(x)):
    s = 0
    while x[i] > 0:
      s += x[i] % 10
      x[i] = int(x[i] / 10)
    res[i] = s
  return res


n = int(input())
a = np.arange(1, n)
b = a[::-1].copy()
print(np.min(sum_of_digits(a) + sum_of_digits(b)))
