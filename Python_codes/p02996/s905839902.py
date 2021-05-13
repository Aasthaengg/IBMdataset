import numpy as np
n = int(input())
g = []
for _ in range(n):
  a, b = map(int, input().split())
  g.append([a,b])
g = np.array(g)
g = g[np.argsort(g[:, 1])]
a = 0
for i,j in g:
  a+=i
  if a>j:
    print('No')
    exit(0)
print('Yes')