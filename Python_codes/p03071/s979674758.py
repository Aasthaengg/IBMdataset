a, b = list(map(int, input().split()))
if a == b:
  my_result = a + b
elif a > b:
  my_result = 2 * a - 1
else:
  my_result = 2 * b - 1
print(my_result)