sa = input()
sb = input()
sc = input()

ended = False
winner = ''
next_turn = 'a'
while not ended:
    if next_turn == 'a':
        if len(sa) == 0:
            ended = True
            winner = 'A'
        else:
            next_turn = sa[0]
            sa = sa[1:]
    elif next_turn == 'b':
        if len(sb) == 0:
            ended = True
            winner = 'B'
        else:
            next_turn = sb[0]
            sb = sb[1:]
    elif next_turn == 'c':
        if len(sc) == 0:
            ended = True
            winner = 'C'
        else:
            next_turn = sc[0]
            sc = sc[1:]
print(winner)
