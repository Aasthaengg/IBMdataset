N = int(input())
A = []

for i in range(N):
  A.append(int(input()))

maxA = max(A)
idx = A.index(maxA)
A.sort()
for i in range(len(A)):
  if i == idx:
    print(max(A[:-1]))
  else:
    print(maxA)
