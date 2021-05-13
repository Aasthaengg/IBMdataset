import numpy as np
N = int(input())
A = [int(x) for x in input().split()]
A = np.array(A)
ans = list()
for i in range(N):
  a = A[i]
  num = 0
  while a%2==0:
    a /= 2.0
    num += 1
  ans.append(num)
print(min(ans))