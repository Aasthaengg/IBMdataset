n = int(input())
F = []
for i in range(n):
  f = list(map(int,input().split()))
  shop = []
  for j in range(5):
    shop.append([f[2*j],f[2*j+1]])
  F.append(shop)
P = [list(map(int,input().split())) for _ in range(n)]

import numpy as np
ans = -float('inf')
for i in range(1,2**10):
  index =format(i,'b').zfill(10)
  open_j = [int(j) for j in index]
  open_j = np.array(open_j).reshape(5,2)
  score = 0
  for j in range(n):
    count = 0
    for k in range(5):
      for l in range(2):
        if F[j][k][l] and open_j[k][l]:
          count += 1
    score += P[j][count]
  ans = max(ans,score)
print(ans)