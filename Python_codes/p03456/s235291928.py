import math
A,B = input().split()
Num = int(A+B)
SqN = math.sqrt(Num)
Flag = False
for T in range(math.floor(SqN),math.ceil(SqN)+1):
    if T*T==Num:
        Flag = True
        break
if Flag:
    print('Yes')
else:
    print('No')