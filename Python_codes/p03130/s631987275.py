A = [0, 0, 0, 0]
for i in range(3):
  x, y = map(int, input().split())
  A[x-1] += 1
  A[y-1] += 1
f = 0
for i in range(4):
  if A[i] == 3:
    print("NO")
    f = 1
    break
if f == 0:
  print("YES")