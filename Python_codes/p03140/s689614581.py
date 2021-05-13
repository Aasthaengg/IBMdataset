n = int(input())
A = input()
B = input()
C = input()
a = [0] * n
for i in range(n):
  if (A[i] == B[i] and A[i] != C[i]):
    a[i] += 1
  elif (A[i] == C[i] and A[i] != B[i]):
    a[i] += 1
  elif (B[i] == C[i] and A[i] != B[i]):
    a[i] += 1
  elif (A[i] == B[i] and B[i] == C[i]):
    a[i] += 0
  else:
    a[i] += 2

print(sum(a))
