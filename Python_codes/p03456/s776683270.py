import math
A,B = input().split()
Num = int(A+B)
SqN = math.sqrt(Num)
if math.floor(SqN)**2==Num or math.ceil(SqN)**2==Num:
    print('Yes')
else:
    print('No')