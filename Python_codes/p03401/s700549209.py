N = int(input())
A = [0] + list(map(int, input().split())) + [0]
B = []
C = []
for i in range(1, N+2):
  B.append(abs(A[i] - A[i-1]))
  if i >= 2:
    C.append(abs(A[i] - A[i-2]))
S = sum(B)
for i in range(1, N+1):
  print(S - B[i-1] - B[i] + C[i-1])