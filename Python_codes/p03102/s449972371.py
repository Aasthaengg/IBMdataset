import numpy as np
N, M, C = map(int, input().split())
b = np.array(list(map(int, input().split())))
cnt = 0

for i in range(N):
  a = np.array(list(map(int, input().split())))
  result = np.dot(a, b) + C
  if result > 0:
    cnt += 1
    
print(cnt)