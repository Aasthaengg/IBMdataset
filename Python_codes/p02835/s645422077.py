a, b, c = list(map(int, input().split()))
n = a + b + c
if n >= 22:
  my_result = 'bust'
else:
  my_result = 'win'
print(my_result)