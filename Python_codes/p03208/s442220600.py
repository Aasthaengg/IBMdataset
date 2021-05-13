import numpy as np
N,K=map(int,input().split())
H=np.array([input() for _ in range(N)],dtype=np.int32)
K-=1
H.sort()
ans=(H[K:]-H[:-K]).min()
print(ans)
