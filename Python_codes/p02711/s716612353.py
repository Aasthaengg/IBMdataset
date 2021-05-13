s = list(input())

flag = True
for i in range(3):
    if '7' == s[i]:
        print('Yes')
        flag = False
        break
if flag:
    print('No')
