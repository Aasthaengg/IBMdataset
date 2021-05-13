A = list(input())
B = list(input())
C = list(input())

next = A.pop(0)
while True:
    if next == 'a':
        if len(A) == 0:
            print('A')
            exit()
        else:
            next = A.pop(0)
    elif next == 'b':
        if len(B) == 0:
            print('B')
            exit()
        else:
            next = B.pop(0)        
    elif next == 'c':
        if len(C) == 0:
            print('C')
            exit()
        else:
            next = C.pop(0)
