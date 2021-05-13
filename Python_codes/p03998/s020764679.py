A =list(str(input()))
B =list(str(input()))
C =list(str(input()))
P=A
for i in range(len(A)+len(B)+len(C)+3):
    if P[0] == 'a':
        P.pop(0)
        P=A
        if len(A) ==0:
            print('A')
            break
    elif P[0] =='b':
        P.pop(0)
        P=B
        if len(B) ==0:
            print('B')
            break
    elif P[0] =='c':
        P.pop(0)
        P=C
        if len(C) ==0:
            print('C')
            break
