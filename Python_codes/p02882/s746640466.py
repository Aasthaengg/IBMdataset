import numpy as np

a,b,x = input().split()
a = int(a)
b = int(b)
x = int(x)
ans = 0
if 2*x/(a**2) < b:
  l = 2*x/(a*b)
  ans = np.arctan(l/b)
else:
  l = 2 * (b - x/(a**2))
  if l == 0:
    ans = np.pi/2
  else:
    ans = np.arctan(a/l)

ans = 90 - np.rad2deg(ans)
print('{:.10f}'.format(ans))