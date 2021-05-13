S = int(input())

A = [1,1,1]

for i in range(3, S - 3 + 1):
  A.append(A[i - 1] + A[i - 3])

if S == 1 or S == 2:
  print(0)
else:
  print(A[S - 3] % (10 ** 9 + 7))