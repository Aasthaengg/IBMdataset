import numpy as np
n = int(input())
argList = np.array(list(map(int, input().split())) )

g = sum(argList % 2 == 0)
k = sum(argList % 2 == 1)

flag = False
if( k % 2 == 0):
    #if( (int(k/2) + g) % 2 == 0):
    flag = True
if flag:
    print('YES')
else:
    print('NO')