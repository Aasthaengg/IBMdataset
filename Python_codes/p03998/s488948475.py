sa = input()
sb = input()
sc = input()

pos_a, pos_b, pos_c = 0, 0, 0
turn = 'a'
while True:
    if turn == 'a':
        if pos_a == len(sa):
            print('A')
            break
        turn = sa[pos_a]
        pos_a += 1

    elif turn == 'b':
        if pos_b == len(sb):
            print('B')
            break
        turn = sb[pos_b]
        pos_b += 1

    else:
        if pos_c == len(sc):
            print('C')
            break
        turn = sc[pos_c]
        pos_c += 1