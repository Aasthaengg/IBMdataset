S = {'A': input(), 'B': input(), 'C': input()}

turn = 'A'

while S[turn] != '':
    next = S[turn][0]
    S[turn] = S[turn][1:]
    turn = next.upper()

print(turn)