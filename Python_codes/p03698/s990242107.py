S = list(input())

flag = 0
for i in S:
    if S.count(i)>1:
        flag = 1
        
if flag == 0:
    print('yes')
else:
    print('no')