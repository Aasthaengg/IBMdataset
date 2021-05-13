a, b = list(map(int, input().split()))
if b % a == 0:
  my_result = a + b
else:
  my_result = b - a
print(my_result)