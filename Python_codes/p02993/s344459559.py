initial_input_num_of_str = input()
double_eyes_list = ['00']

# 4桁の数字を、３つに分ける。最初２文字、真ん中２文字、後ろ２文字
first_numbers = initial_input_num_of_str[0:2]
center_numbers = initial_input_num_of_str[1:3]
last_numbers = initial_input_num_of_str[-2:]

for i in range(11, 100, 11):
    double_eyes_list.append(str(i))

if first_numbers in double_eyes_list:
    print('Bad')
elif center_numbers in double_eyes_list:
    print('Bad')
elif last_numbers in double_eyes_list:
    print('Bad')
else:
    print('Good')