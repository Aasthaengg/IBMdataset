a, b, k = map(int, input().split())
for i in range(k):
  if i % 2 == 0:
    if a % 2 != 0:
      a = a - 1
    a = a // 2
    b = b + a
  else:
    if b % 2 != 0:
      b = b - 1
    b = b // 2
    a = a + b
print(a, end=" ")
print(b)