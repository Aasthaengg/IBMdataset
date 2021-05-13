N = int(input())
a = N % 10
if a == 3:
  my_result = 'bon'
elif a == 0 or a == 1 or a == 6 or a == 8:
  my_result = 'pon'
else:
  my_result = 'hon'
print(my_result)