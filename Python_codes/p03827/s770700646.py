n = int(input())
s = input()

x = 0
x_max = 0
s_list = []

for i in s:
    s_list.append(i)

# print(s_list)

for i in s_list:
    if i == 'I':
        x += 1
        if x > x_max:
            x_max = x
    elif i == 'D':
        x -= 1


print(x_max)
