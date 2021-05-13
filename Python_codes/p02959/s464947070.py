n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a1 = sum(A)
for i in range(n):
  b = B[i]
  if A[i] >= b:A[i] -= b
  else:
    if A[i+1]+A[i] >= b:
      A[i+1] = A[i+1]+A[i]-b
      A[i] = 0
    else:A[i], A[i+1] = 0, 0
a2 = sum(A)
print(a1-a2)