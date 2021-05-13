# coding: utf-8
a=int(input())
b=int(input())
la=len(str(a))
lb=len(str(b))

if la>lb:
    print('GREATER')
elif la<lb:
    print('LESS')
else:
    Flg=True
    for i in range(la):
        if int(str(a)[i])>int(str(b)[i]):
            print('GREATER')
            Flg=False
            break
        elif int(str(a)[i])<int(str(b)[i]):
            print('LESS')
            Flg=False
            break
    if Flg:
        print('EQUAL')