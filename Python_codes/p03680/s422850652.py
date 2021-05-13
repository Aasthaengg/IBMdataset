N = int(input())
A = {}
for i in range(N):
  A[i+1] = int(input())
B = [-1 for i in range(N+1)]
B[1] = 0
i = 1
while 1:
  j = A[i]
  if j == 2:
    print(B[i] + 1)
    break
  elif B[j] != -1:
    print(-1)
    break
  else:
    B[j] = B[i] + 1
    i = j