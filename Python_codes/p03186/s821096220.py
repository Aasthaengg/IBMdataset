a, b, c = map(int, input().split())
if c > (a + b):
  num = a + 2*b + 1
else:
  num = b + c
print(num)