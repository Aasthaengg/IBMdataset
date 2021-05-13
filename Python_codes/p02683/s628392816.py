import numpy as np

n,m,x = map(int,input().split())
ca = list(list(map(int,input().split())) for _ in range(n))

ans = 10**7
for i in range(1,2**n):
  l = []
  for j in range(n):
    if (i >> j) & 1:
      l.append(ca[j])
  s = np.sum(l,axis=0).tolist()
  if all(s[k] >= x for k in range(1,m+1)) and s[0] < ans:
    ans = s[0]

if ans == 10**7:
  print(-1)
else:
  print(ans)