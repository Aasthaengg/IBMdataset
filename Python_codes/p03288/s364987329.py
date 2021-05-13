n = int(input())
if n < 1200:
  my_result = 'ABC'
elif n >= 1200 and n < 2800:
  my_result = 'ARC'
else:
  my_result = 'AGC'
print(my_result)