n = int(input())
l = n
if not n % 2:
  l += 1
print(n * (n - 1) // 2 - n // 2 )
for i in range(1, n+1):
  for j in range(i+1, n+1):
    if i + j == l:
      continue
    print(i, j)