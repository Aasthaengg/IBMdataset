import numpy as np
N = int(input())
A = np.array([int(x) for x in input().split()])
mi= np.min(A)
ma= np.max(A)
mai = np.where(A==ma)
mii = np.where(A==mi)
ans = []
if ma<=0 and mi<=0:
  for i in range(N,1,-1):
    ans.append((i,i-1))
  print(len(ans))
  for i in range(len(ans)):
    print(*ans[i])
  exit()
if ma>=0 and mi>=0:
  for i in range(1,N):
    ans.append((i,i+1))
  print(len(ans))
  for i in range(len(ans)):
    print(*ans[i])
  exit()

if abs(mi)<=abs(ma):
  ans= [(int(mai[0][0])+1,i) for i in range(1,N+1)]
  for i in range(1,N):
    ans.append((i,i+1))
  print(len(ans))
  for i in range(len(ans)):
    print(*ans[i])
  exit()
else:
  ans= [(int(mii[0][0])+1,i) for i in range(1,N+1)]
  for i in range(N,1,-1):
    ans.append((i,i-1))
  print(len(ans))
  for i in range(len(ans)):
    print(*ans[i])
  exit()