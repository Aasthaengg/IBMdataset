a, b, c = list(map(int, input().split()))
my_result = c - a + b
if my_result >= 0:
  print(my_result)
else:
  print(0)