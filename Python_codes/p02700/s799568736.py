turn = "A"
A, B, C, D = map(int, input().split(' '))

while A > 0 and B > 0:
    if turn == "A":
        C -= B
        turn = "C"
        if not C > 0:
            print('Yes')
            break
    else:
        A -= D
        turn = "A"
        if not A > 0:
            print('No')
            break