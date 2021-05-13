S = input()
T = input()
flag = 0
for i in range(len(S)):
    S = S[-1]+S[0:-1]
    if S == T:
        flag = 1
        break
if flag == 1:
    print('Yes')
else:
    print('No')
