import numpy as np
N,K=map(int, input().split())
X=list(map(int, input().split()))
ans=np.inf
for i in range(N-K+1):
  l=X[i]
  r=X[i+K-1]
  ans=min(ans, r-l+min(abs(l), abs(r)))
print(ans)