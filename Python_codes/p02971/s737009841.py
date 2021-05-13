N = int(input())
A = [0]*N
for i in range(N):
  A[i] = int(input())
B = sorted(A)
for i in range(N):
  if A[i] == B[-1]:
    print(B[-2])
  else:
    print(B[-1])