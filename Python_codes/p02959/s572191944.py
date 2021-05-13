n = int(input())
a = [int(e) for e in input().split()]
b = [int(e) for e in input().split()]
result = 0
for i in range(n):
  if a[i] > b[i]:
    result += b[i]
    b[i] = 0
  else:
    result += a[i]
    b[i] -= a[i]
    if a[i + 1] > b[i]:
      result += b[i]
      a[i + 1] -= b[i]
    else:
      result += a[i + 1]
      a[i + 1] = 0
print(result)