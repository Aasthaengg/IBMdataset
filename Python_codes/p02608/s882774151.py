import math
N =int(input())
M = int(math.sqrt(N))
ans = [0 for _ in range(10050)]
for j in range(M):
  for k in range(M):
    for l in range(M):
      v = (j+1)**2 + (k+1)**2 + (l+1)**2 + (j+1)*(k+1) + (k+1)*(l+1) + (l+1)*(j+1)
      if (v<=N):
        ans[v] += 1
for i in range(N):
  print(ans[i+1])