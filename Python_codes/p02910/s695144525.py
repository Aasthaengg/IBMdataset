S = str(input())
check = 1
for i in range(len(S)):
    if i%2==0 and S[i]=='L':
        check = 0
        break
    elif i%2==1 and S[i]=='R':
        check = 0
        break
if check == 1:
    print('Yes')
else:
    print('No')