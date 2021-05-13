import numpy as np
N, T = list(map(int, input().split()))
t = np.array(list(map(int, input().split())))
tT = np.sort(t)[::-1] + T

total = tT[0]
for i in range(1, N):
  total -= max(tT[i-1] - tT[i]-T, 0)
  
print(total)
  
