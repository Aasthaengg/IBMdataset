S = list(input())
T = list(input())
flag = 0
for i in range(len(S)):
    if S == T:
        flag = 1
        break
    tmp = S.pop(0)
    S.append(tmp)
if flag == 1:
    print('Yes')
else:
    print('No')