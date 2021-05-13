import numpy as np
N, M = map(int, input().split())
ans = np.zeros(M)
for i in range(N):
  KA = list(map(int, input().split()))
  for j in range(KA[0]):
    idx = KA[j+1]-1
    ans[idx] += 1

count = 0
for i in range(M):
  if ans[i] == N:
    count += 1
print(count)