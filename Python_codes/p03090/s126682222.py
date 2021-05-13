n = int(input())
a = []
b = []
for i in range(n):
  for j in range(i+1, n):
    a.append([i+1, j+1])
if n % 2 == 0:
  for i in range(len(a)):
    if a[i][0] + a[i][1] != n + 1:
      b.append(a[i])
else:
  for i in range(len(a)):
    if a[i][0] + a[i][1] != n:
      b.append(a[i])
m = len(b)
print(m)
for i in range(m):
  print(b[i][0], b[i][1])
