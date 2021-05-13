import numpy as np

N = int(input())
C = np.array([input().split() for i in range(N)])
sm = 0
for i in range(N):
    sm += int(C[i, 1])-int(C[i, 0])+1

print(sm)