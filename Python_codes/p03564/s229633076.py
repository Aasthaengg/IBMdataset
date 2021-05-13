a = int(input())
b = int(input())
n = 1
for i in range(a):
  if n * 2 <= n + b:
    n *= 2
  else:
    n += b
print(n)