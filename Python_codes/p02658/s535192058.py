import numpy as np

N = int(input())
Alist = list(map(int,input().split()))

#ans = np.prod(Alist)
Alist.sort()
ans = 1
for i in range(N):
  #print (Alist[i])
  ans*= Alist[i]
  if Alist[i]==0:
    break
  if ans >10**18:
    break

if ans >10**18:
  print(-1)
else:
  print(ans)
