n = int(input())
s = input()

s_list = []

for item in s:
    if item == '.':
        s_list.append(0)
    else:
        s_list.append(1)

min_val = s_list.count(0)

left_val = 0
right_val = s_list.count(0)

for i in range(len(s_list)):
    if s_list[i] == 0:
        right_val -= 1
        min_val = min(left_val + right_val, min_val)
    else:
        left_val += 1

print(min_val)
