a, b, c = (int(i) for i in input().split())
if a + b + 1 >= c:
  result = b + c
else:
  result = a + 2 * b + 1
print(result)