N = int(input())
A = [[int(input()), i] for i in range(N)]
A.sort(reverse=True)

ex = A[0]
nx = A[1]

for i in range(N):
  if i == ex[1]:
    print(nx[0])
  else:
    print(ex[0])