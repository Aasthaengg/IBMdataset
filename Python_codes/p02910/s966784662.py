S=input()

odd=['R','U','D']
even=['L','U','D']
flag=True
for i in range(len(S)):
    if (i+1)%2==0 and not(S[i] in even):
        flag=False
        print('No')
        break 
    elif (i+1)%2==1 and not(S[i] in odd):
        flag=False
        print('No')
        break

if flag:
    print('Yes')
