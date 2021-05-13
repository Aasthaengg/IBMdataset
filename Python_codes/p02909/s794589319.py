S = input()
print_list = ['Sunny', 'Cloudy', 'Rainy']
value = 1 + (print_list.index(S))
if value == 3:
    value = 0
print(print_list[value])
