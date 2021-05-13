import numpy as np
N = int(input())
R = np.array([list(map(int,input().split())) for n in range(N)])
print(sum(np.linalg.norm(i-j) for i in R for j in R)/N)