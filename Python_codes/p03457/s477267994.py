N = int(input())
TB,XB,YB = 0,0,0
Flag = True
for Z in range(0,N):
    TA,XA,YA = (int(A) for A in input().split())
    RestT = (TA-TB)-(abs(XA-XB)+abs(YA-YB))
    if RestT<0 or RestT%2!=0:
        Flag = False
        break
    else:
        TB,XB,YB = TA,XA,YA
if Flag:
    print('Yes')
else:
    print('No')