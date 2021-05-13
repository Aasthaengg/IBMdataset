import numpy as np
n, m = map(int, input().split())
a = list(map(int, input().split()))
flag = False
c = []
for _ in range(m):
  x,y = map(int, input().split())
  c.append([x,y])
c = np.array(c)
e = c[np.argsort(c[:, 1])]
d = []
for x,y in reversed(e):
  for i in range(x):
    d.append(y)
    if len(d) == n:
      flag = True
      break
  if flag:
    break
f = sorted(a+d,reverse=True)
print(sum(f[:n]))