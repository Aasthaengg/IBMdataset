S = input()

cnt = 0
for i in S:
    if(i=='o'):
        cnt += 1
if(15-len(S)+cnt>=8):
    print('YES')
else:
    print('NO')
