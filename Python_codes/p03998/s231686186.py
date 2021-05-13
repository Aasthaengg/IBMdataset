SA = input()
SB = input()
SC = input()
la = len(SA)
lb = len(SB)
lc = len(SC)
turn = SA[0]
ai = 0
bi = 0
ci = 0
while True:
    if turn == 'a':
        if ai == la:
            print('A')
            break
        turn = SA[ai]
        ai += 1
    elif turn == 'b':
        if bi == lb:
            print('B')
            break
        turn = SB[bi]
        bi += 1
    else:
        if ci == lc:
            print('C')
            break
        turn = SC[ci]
        ci += 1


