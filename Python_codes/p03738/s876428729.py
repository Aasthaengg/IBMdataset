A,B = (int(input()) for T in range(0,2))
if A==B:
    print('EQUAL')
else:
    print(['GREATER','LESS'][A<B])