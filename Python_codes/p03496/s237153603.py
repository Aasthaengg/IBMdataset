n = int(input())
print(2 * (n - 1))
a = list(map(int, input().split()))
index = 0
for i in range(1, n):
  if abs(a[i]) > abs(a[index]):
    index = i
if a[index] >= 0:
  for i in range(1, n):
    a[i] += a[index]
    print(index + 1, i + 1)
    if abs(a[i]) > abs(a[index]):
      index = i
    a[i] += a[index]
    print(index + 1, i + 1)
    if abs(a[i]) > abs(a[index]):
      index = i
else:
  for i in range(n - 2, -1, -1):
    a[i] += a[index]
    print(index + 1, i + 1)
    if abs(a[i]) > abs(a[index]):
      index = i
    a[i] += a[index]
    print(index + 1, i + 1)
    if abs(a[i]) > abs(a[index]):
      index = i
