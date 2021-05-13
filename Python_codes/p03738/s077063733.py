A=int(input())
B=int(input())
if A==B:
    print('EQUAL')
else:
    print(['GREATER','LESS'][A<B])