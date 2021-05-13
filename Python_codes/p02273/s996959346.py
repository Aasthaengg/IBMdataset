import math

def rotate(x, y):
  r3 = math.sqrt(3)
  x2 = x / 2 - y * r3 / 2
  y2 = x * r3 / 2 + y / 2
  return x2, y2

def divide(a, b):
  m1 = [(b[0] - a[0]) / 3 + a[0], (b[1] - a[1]) / 3 + a[1]]
  m2 = [(b[0] - a[0]) * 2 / 3 + a[0], (b[1] - a[1]) * 2 / 3 + a[1]]
  r = rotate(m2[0] - m1[0], m2[1] - m1[1])
  m = [m1[0] + r[0], m1[1] + r[1]]
  return (a, m1, m, m2, b)

n = int(input())
arr = ([0, 0], [100, 0])

for i in range(n):
  tmp = []
  for j in range(len(arr) - 1):
    r = divide(arr[j], arr[j + 1])
    if j > 0: r = r[1:]
    tmp += r
  arr = tmp

for a in arr:
  print(" ".join(map(lambda x: str(round(x, 8)), a)))