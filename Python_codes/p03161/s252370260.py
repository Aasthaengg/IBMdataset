import numpy as np

N, K = map(int, input().split())
hs = np.array(list(map(int, input().split())))

i = 0
total_cost = 0
 
a = np.zeros(N, dtype=np.int64)
a[0] = 0
a[1] = abs(hs[1] - hs[0])

for i in range(2, N):
    k = min(K,i)
    a[i] = np.min(a[i-k:i] + np.abs(hs[i] - hs[i-k:i]))    
print(a[-1])
