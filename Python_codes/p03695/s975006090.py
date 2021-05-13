N = int(input())
A = list(map(int, input().split()))
B = []
C = 0
for i in range(N):
  if A[i]//400 < 8:
    B.append(A[i]//400)
  else:
    C += 1
b = set(B)
if len(b) == 0:
  print(1, C)
else:
  print(len(b), len(b)+C)