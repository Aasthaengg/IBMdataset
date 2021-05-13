a, b, k = [int(i) for i in input().split()]

for i in range(k):
  if i % 2 == 0:
    b += a // 2
    a = a // 2
  else:
    a += b // 2
    b = b // 2
print(a, b)