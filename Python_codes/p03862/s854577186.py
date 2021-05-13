N, x = map(int, input().split())
A = list(map(int, input().split()))
sumA = sum(A)
for i in range(1,N):
  diff = A[i] + A[i-1] - x
  if diff > 0:
    if diff <= A[i]:
      A[i] -= diff
    else:
      A[i-1] -= diff - A[i]
      A[i] = 0
print(sumA - sum(A))