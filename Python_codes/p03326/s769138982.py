import numpy as np
n,m,*xyz = map(int,open(0).read().split())
xyz = np.array(xyz).reshape(n,3)
abs_pattern = np.array(np.meshgrid((1,-1),(1,-1),(1,-1))).reshape(-1,3)
if m==0:
    ans = 0
else:
    ans = np.sort(np.dot(abs_pattern,xyz.T))[:,-m:].sum(axis=1).max()
print(ans)