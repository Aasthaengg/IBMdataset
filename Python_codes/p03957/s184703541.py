S = input()
flag = 0
for i in range(len(S)):
    if S[i] == 'C':
        flag = 1
    elif S[i] == 'F' and flag:
        print('Yes')
        break
else:
    print('No')