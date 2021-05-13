N = int(input())
K = int(input())
A = 1
for i in range(N):
  if A > K:
    A += K
  else:
    A *= 2
else:
  print(A)