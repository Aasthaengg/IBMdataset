A = input()
B = input()
if A == B:
    print('EQUAL')
elif len(A) > len(B):
    print('GREATER')
elif len(B) > len(A):
    print('LESS')
else:
    for i in range(len(A)):
        a = int(A[i])
        b = int(B[i])
        if a > b:
            print('GREATER')
            break
        elif b > a:
            print('LESS')
            break