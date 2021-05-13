A, B, C = [list(input()) for _ in range(3)]
x = 'a'
while True:
    if x == 'a':
        if len(A) == 0:
            print('A')
            exit()
        x = A[0]
        A.remove(x)
    elif x == 'b':
        if len(B) == 0:
            print('B')
            exit()
        x = B[0]
        B.remove(x)   
    elif x == 'c':
        if len(C) == 0:
            print('C')
            exit()
        x = C[0]
        C.remove(x)   
