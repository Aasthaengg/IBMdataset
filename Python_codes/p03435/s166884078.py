import numpy as np
Num = np.zeros((3,3),dtype=int)
Flag = False
for T in range(0,3):
    Num[T,:] = np.array([int(X) for X in input().split()])
for T in range(0,3):
    Num[:,T] -= Num[0,T]
for A2 in range(min(Num[1,:]),max(Num[1,:])+1):
    AB2 = np.array([A2+Num[0,0],A2+Num[0,1],A2+Num[0,2]])
    if np.all(AB2==Num[1,:]):
        for A3 in range(min(Num[2,:]),max(Num[2,:])+1):
            AB3 = np.array([A3+Num[0,0],A3+Num[0,1],A3+Num[0,2]])
            if np.all(AB3==Num[2,:]):
                Flag = True
                break
    if Flag:
        break     
if Flag:
    print('Yes')
else:
    print('No')