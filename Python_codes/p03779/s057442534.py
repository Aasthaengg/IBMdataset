from math import sqrt
x = int(input())
t = 0
while t>=0:
  if 2*x <= t**2+t:
    print(t)
    break
  t += 1