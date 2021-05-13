import numpy as np
n,p = map(int, input().split())
alist = map(int, input().split())
x = np.array([[2,0],[0,2]])
y = np.array([[1,1],[1,1]])
ans = np.array([1,0])
for a in alist:
  if a%2 == 0:
    ans = np.dot(x,ans)
  if a%2 == 1:
    ans = np.dot(y,ans)
print(ans[p])