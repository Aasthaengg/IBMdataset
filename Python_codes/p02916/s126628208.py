N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
K = 0 
for i in range(N):
  if i == 0:
    K += B[A[i] - 1]
  else:
    K += B[A[i] - 1]
    if A[i] == A[i - 1] + 1:
      K += C[A[i - 1] - 1]
print(K)