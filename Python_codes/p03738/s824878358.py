a = input()
b = input()
if len(a)<len(b):
    print('LESS')
elif len(a)>len(b):
    print('GREATER')
else:
    for aa, bb in zip(a, b):
        if aa<bb:
            print('LESS')
            break
        elif aa>bb:
            print('GREATER')
            break
    else:
        print('EQUAL')