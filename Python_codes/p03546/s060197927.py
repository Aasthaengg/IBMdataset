from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from scipy.sparse.csgraph import floyd_warshall

h,w=nii()
c=[lnii() for i in range(10)]
a=[lnii() for i in range(h)]

s=floyd_warshall(c)

ans=0
for i in range(h):
  for j in range(w):
    if a[i][j]==-1:
      continue
    ans+=s[a[i][j]][1]
print(int(ans))