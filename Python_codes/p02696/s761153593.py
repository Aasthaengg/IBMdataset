from math import floor

a, b, n = map(int, input().split())

max_v = 0
if n < b:
  max_v = floor(a * n / b)
else:
  if b != 1:
    for i in range(b - 1, n + 1, b):
      j = 0
      t = floor(a * i / b) - a * j
      if t > max_v:
        max_v = t
      j += 1
print(max_v)