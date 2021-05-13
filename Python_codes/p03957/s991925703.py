s = input()
flag = False
for i in range(len(s)):
    if s[i] == 'C':
        flag = True
    if flag and s[i] == 'F':
        print('Yes')
        exit()
print('No')
