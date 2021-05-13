n, a, b = list(map(int, input().split()))
x = 0
if n * a < b:
  x = n * a
else:
  x = b
print(x)