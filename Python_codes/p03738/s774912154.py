A,B = (input() for T in range(0,2))
if len(A)!=len(B):
    print(['GREATER','LESS'][len(A)<len(B)])
else:
    EqualFlag = True
    for TL in range(0,len(A)):
        if A[TL]!=B[TL]:
            EqualFlag = False
            break
    if EqualFlag:
        print('EQUAL')
    else:
        print(['GREATER','LESS'][A[TL]<B[TL]])