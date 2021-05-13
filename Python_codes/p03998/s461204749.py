A = list(input()[::-1])
B = list(input()[::-1])
C = list(input()[::-1])
turn = 'a'
while True:
    if turn == 'a':
        if not A:
            print('A')
            break
        turn = A.pop()
    elif turn == 'b':
        if not B:
            print('B')
            break
        turn = B.pop()
    else:
        if not C:
            print('C')
            break
        turn = C.pop()