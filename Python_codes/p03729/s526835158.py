A,B,C = map(str,input().split())

flag = True
if A[-1] != B[0]:
    flag = False

if B[-1] != C[0]:
    flag = False

if flag:
    print('YES')
else:
    print('NO')