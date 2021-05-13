import numpy as np
N, M, C = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
B = np.array(B)
ans = 0
for i in range(N):
  A = [int(x) for x in input().split()]
  A = np.array(A)
  if(sum(A*B)+C)>0:
    ans += 1
print(ans)