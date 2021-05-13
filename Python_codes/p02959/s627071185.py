N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
for i in range(N):
  if A[i] >= B[i]:
    count += B[i]
  elif A[i] < B[i]:
    count += A[i]
    B[i] -= A[i]
    A[i] = 0
    if A[i+1] >= B[i]:
      count += B[i]
      A[i+1] -= B[i]
    else:
      count += A[i+1]
      A[i+1] = 0
print(count)