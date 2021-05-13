import numpy as np
N,X = map(int, input().split())
L = list(map(int, input().split()))

dist = np.zeros(N+1, dtype=int)
for i in range(N):
  dist[i+1] = dist[i] + L[i]

i = 0
count = 0
while dist[i] <= X:
  count += 1
  i += 1
  if i == N +1:
    break
print(count)
"""
dist = 0
count = 1
for i in range(N):
  if dist + L[i] <= X:
    count += 1
    dist += L[i]
print(count)
"""