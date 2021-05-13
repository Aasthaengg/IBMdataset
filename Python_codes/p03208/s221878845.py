import numpy as np

N,K,*H = map(int,open(0).read().split())
H =np.array(sorted(H))

H = np.diff(H,n=1)
minH = 1e10

for i in range(N-K+1):
  minH = min(H[i:i+K-1].sum(),minH)
  #print(i,H[i:i+K-1])
print(minH)