n = input()
number = ''
for i in n:
    # print(f"i = {i}")
    if i == '1':
        i = '9'
    elif i == '9':
        i = '1'
    number += i
print(int(number))
