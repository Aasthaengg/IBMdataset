s = list(input())
for i in s[::2]:
    if i == 'L':
        print('No')
        exit()
for j in s[1::2]:
    if j == 'R':
        print('No')
        exit()
print('Yes')