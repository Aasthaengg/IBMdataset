A = list(input())
B = list(input())
C = list(input())

def turn(card):
    if card == 'a':
        if A:
            turn(A.pop(0))
        else:
            print('A')
            exit(0)
    elif card == 'b':
        if B:
            turn(B.pop(0))
        else:
            print('B')
            exit(0)
    else:
        if C:
            turn(C.pop(0))
        else:
            print('C')
            exit(0)

turn(A.pop(0))