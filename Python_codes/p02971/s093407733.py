import copy
N = int(input())
A = []
for i in range(N):
  tmp = int(input())
  A.append(tmp)

B = copy.copy(A)
B.sort()

max_val = max(B)
for i in range(N):
  if A[i] == max_val:
    print(B[N-2])
  else:
    print(B[N-1])