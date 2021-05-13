import numpy as np
N = int(input())
l,r = np.array([0]*N),np.array([0]*N)
for i in range(N):
    l[i],r[i] = map(int, input().split())
rl = r-l+1
print(sum(rl))