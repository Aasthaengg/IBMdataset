import copy
n = int(input())
a = list(map(int, input().split()))
b = [0]*n
for i in range(n, 0, -1):
  c = 0
  for j in range(i - 1, n, i):
    c += b[j]
  if c%2 != a[i - 1]:
    b[i - 1] = 1

if sum(b) == 0:
  print(0)
else:
  print(sum(b))
  for i in range(n):
    if b[i] == 1:
      print(str(i + 1), end=" ")