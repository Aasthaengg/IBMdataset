s = input()
flag = 0

for i in s:
    if i == 'C':
        flag = 1
    if i == 'F' and flag == 1:
        print('Yes')
        exit()
print('No')
