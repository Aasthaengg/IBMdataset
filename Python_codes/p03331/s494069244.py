n = int(input())
l = []
for i in range(1, n // 2 + 1):
  a = str(i)
  b = str(n - i)
  k = 0
  for j in range(len(a)):
    k += int(a[j])
  for j in range(len(b)):
    k += int(b[j])
  l.append(k)
print(min(l))