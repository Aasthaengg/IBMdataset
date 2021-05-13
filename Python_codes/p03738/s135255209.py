A = input()
B = input()
if A == B:
    print('EQUAL')
    exit()
if len(A) > len(B):
    print('GREATER')
elif len(A) < len(B):
    print('LESS')
else:
    for i in range(len(A)):
        if int(A[i]) > int(B[i]):
            print('GREATER')
            break
        elif int(A[i]) < int(B[i]):
            print('LESS')
            break