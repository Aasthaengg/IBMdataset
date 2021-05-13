import numpy as np
N = int(input())

m = {}
for i in range(1, N + 1):
  x = str(i)
  if '0' in [x[0], x[-1]]:
    continue
  key = str([x[0], x[-1]])
  add = 1
  
  if key not in m:
    m[key] = add
  else:
    m[key] += add

ans = 0
for i in range(1, 10):
  for j in range(1, 10):
    key = str([str(i), str(j)])
    if key in m:
      d = m[key]
      if i == j:
        ans += d ** 2
      elif str([str(j),str(i)]) in m:
        ans += d * m[str([str(j),str(i)])]
    
print(ans)