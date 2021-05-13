n = int(input())
a = 100000
for i in range(n):
  a = a * 1.05
  b = 0
  if a % 1000:
    b = 1000
  a = int(a // 1000 * 1000 + b)
print(a)
