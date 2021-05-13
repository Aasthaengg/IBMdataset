N,K=map(int,input().split())
X=list(map(int,input().split()))
import numpy as np
a=np.searchsorted(X, 0, side='left')
if a==N:
  X=np.insert(X,a,0)
  N+=1
  K+=1
elif X[a]!=0:
  X=np.insert(X,a,0)
  N+=1
  K+=1
ans=10**18
i=a-K+1 if K-1<a else 0
while i<=a and i+K-1<N:
  l=-X[i]
  r=X[i+K-1]
  if l>r:
    l,r=r,l
  ans=min(ans,2*l+r)
  i+=1
print(ans)