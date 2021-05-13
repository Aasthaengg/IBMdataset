count = 0
N = int(input())
A = input()
B = input()
C = input()
for i in range(N):
  if A[i] == B[i] and B[i] == C[i]:
    count = count
  elif A[i] == B[i] or B[i] == C[i] or C[i] == A[i]:
    count = count + 1
  else:
    count = count + 2
print(count)