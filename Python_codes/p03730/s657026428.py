A, B, C = map(int, input().split())
i = 1
flag = False
while(A*i < A*B):
    if A*i%B == C:
        flag = True
        break
    i+=1

if(flag):
    print('YES')
else:
    print('NO')