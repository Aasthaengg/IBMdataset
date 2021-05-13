import sys
A = list(input())
B = list(input())
C = list(input())
A = A[::-1]
B = B[::-1]
C = C[::-1]
X = 0
while True:
    if X == 0:
        if A:
            S = A.pop()
            if S == 'a':
                X = 0
            elif S == 'b':
                X = 1
            else:
                X = 2
        else:
            print('A')
            sys.exit()
    elif X == 1:
        if B:
            S = B.pop()
            if S == 'a':
                X = 0
            elif S == 'b':
                X = 1
            else:
                X = 2
        else:
            print('B')
            sys.exit()
    else:
        if C:
            S = C.pop()
            if S == 'a':
                X = 0
            elif S == 'b':
                X = 1
            else:
                X = 2
        else:
            print('C')
            sys.exit()