N = int(input())
A = list(map(int, input().split()))
t = sum(A)
B = [0] * N
for i in range(0, N, 2):
  B[0] += A[i]
B[0] = 2 * B[0] - t

for i in range(1,N):
  B[i] = 2 * A[i-1] - B[i-1]

for i in range(N):
  print(B[i],end=" ")