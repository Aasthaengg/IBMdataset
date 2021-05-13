a, b, k = map(int, input().split())
for i in range(k):
  if i % 2 == 0:
    if a % 2 == 1:
      a -= 1
    num = a // 2
    a, b = a - num, b + num
  else:
    if b % 2 == 1:
      b -= 1
    num = b // 2
    a, b = a + num, b - num
print(a, b)