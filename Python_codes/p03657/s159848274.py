A, B = map(int,input().split())
flag = 0
for i in (A, B, A+B):
    if i % 3 == 0:
        flag = 1
if flag:
    print('Possible')
else:
    print('Impossible')