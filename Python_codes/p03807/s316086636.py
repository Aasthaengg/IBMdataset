N=int(input())
A=list(map(int,input().split()))


import numpy as np
A=np.array(A)
B=list(A%2)
if B.count(1)%2==1:
    print('NO')
else:
    print('YES')