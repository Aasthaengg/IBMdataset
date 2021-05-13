def f(L, i, j):
  h = len(L)
  w = len(L[0])
  if L[i][j] != ".":
    return L[i][j]
  else:
    around = [L[i-1][j-1], L[i-1][j], L[i-1][j+1], L[i][j-1], L[i][j+1], L[i+1][j-1], L[i+1][j], L[i+1][j+1]]
    return str(around.count("#"))

H, W = list(map(lambda x: int(x), input().split(" ")))
A = []
A.append(["X"] * (W + 2))
for i in range(H):
  A.append(["X"])
  A[i + 1].extend(list(input()))
  A[i + 1].extend(["X"])
A.append(["X"] * (W + 2))

for i in range(len(A)):
  for j in range(len(A[0])):
    A[i][j] = f(A, i, j)

print("\n".join(["".join(a[1:-1]) for a in A[1:-1]]))