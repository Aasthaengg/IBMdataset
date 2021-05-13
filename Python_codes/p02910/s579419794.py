a = ['R','U','D']
b = ['L','U','D']
s = input()
flag = True
for i in range(len(s)):
    if (i+1) % 2 == 0:
        if s[i] not in b:
            flag = False
    else:
        if s[i] not in a:
            flag = False

if flag:
    print('Yes')
else:
    print('No')