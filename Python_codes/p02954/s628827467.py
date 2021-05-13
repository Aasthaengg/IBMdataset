import numpy as np

S = input()
N = len(S)
ans = np.zeros(N, dtype=np.int)

j = 0
for i in range(0,N-1):
  if j != 0:
    j -= 1
  if j == 0:
    while S[i+j] == 'R':
      j += 1
  if j != 0:
    if j % 2 == 0:
      ans[i+j] += 1
    else:
      ans[i+j-1] += 1

j = 0
for i in range(N-1, 0, -1):
  if j != 0:
    j -= 1
  if j == 0:
    while S[i-j] == 'L':
      j += 1
  if j != 0:
    if j % 2 == 0:
      ans[i-j] += 1
    else:
      ans[i-j+1] += 1
print(*ans)