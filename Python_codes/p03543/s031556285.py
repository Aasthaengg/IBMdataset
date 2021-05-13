n = input()

onaji = 0

flag = False

for i in range(3):
    if n[i] == n[i+1]:
        onaji += 1
        if onaji >= 2:
            flag = True
    else:
        onaji = 0
        
if flag == True:
    print('Yes')
else:
    print('No')