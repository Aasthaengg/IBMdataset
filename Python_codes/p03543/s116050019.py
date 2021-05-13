int_str = input()
triple_same_digit = ['000']

first_three_digits = int_str[0:3]
last_three_digits = int_str[-3:]

for i in range(111, 1000, 111):
    triple_same_digit.append(str(i))

if first_three_digits in triple_same_digit:
    print('Yes')
elif last_three_digits in triple_same_digit:
    print('Yes')
else:
    print('No')