numbers = input()
number_list = [int(i) for i in numbers.split()]
if number_list[0] <= number_list[2] and number_list[2] <= number_list[1]:
  print('Yes')
else:
  print("No")