n = str(input())
flag = False

for i in range(2):
    if '9' in n[i]:
        flag = True
        break
        
if flag:
    print('Yes')
else:
    print('No')
