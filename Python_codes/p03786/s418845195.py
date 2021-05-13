import numpy as np
N = int(input())
M = [0] + sorted(list(map(int, input().split())))
C = np.cumsum(M)
#print(M, C)
#2分探索とかでも良さそうだけど
for i in range(N-1, -1, -1):
  #print(M[i], C[i+1])
  if C[i]*2 < M[i+1]:
    #print(i)
    break
print(N-i)
