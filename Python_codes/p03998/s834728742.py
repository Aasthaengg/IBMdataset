sa = list(input()+'x')
sb = list(input()+'x')
sc = list(input()+'x')

card = sa.pop(0)
turn = 'A'
while card != 'x':
    if card == 'a':
        card = sa.pop(0)
        turn = 'A'
    elif card == 'b':
        card = sb.pop(0)
        turn = 'B'
    else:
        card = sc.pop(0)
        turn = 'C'
print(turn)
