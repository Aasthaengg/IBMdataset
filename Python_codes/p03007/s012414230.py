n = int(input())
A = sorted(map(int, input().split()))
L = []
if A[0] >= 0:
  x = A[0]
  for i in range(1, n-1):
    L.append((x, A[i]))
    x -= A[i]
  L.append((A[-1], x))
  M = A[-1] - x
elif A[-1] < 0:
  x = A[-1]
  for i in range(1, n):
    L.append((x, A[n-1-i]))
    x -= A[n-1-i]
  M = x
else:
  for i in range(n):
    if A[i] >= 0:
      border = i
      break
  for i in range(border, n-1):
    L.append((A[0], A[i]))
    A[0] -= A[i]
  x = A[-1]
  for i in range(border):
    L.append((x, A[i]))
    x -= A[i]
  M = x
  
print(M)
for x, y in L:
  print(x, y)