A = input()
B = input()

if len(A) != len(B):
    if len(A) > len(B):
        print('GREATER')
    else:
        print('LESS')
else:
    for a, b in zip(A, B):
        if int(a) > int(b):
            print('GREATER')
            exit()
        elif int(a) < int(b):
            print('LESS')
            exit()
    print('EQUAL')