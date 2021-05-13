n = int(input())
A = input()
B = input()
C = input()
a = [0] * n
for i in range(n):
  if (A[i] == B[i] == C[i]):
    a[i] += 0
  elif (A[i] == B[i] or B[i] == C[i] or A[i] == C[i]):
    a[i] += 1
  else:
    a[i] += 2

print(sum(a))
