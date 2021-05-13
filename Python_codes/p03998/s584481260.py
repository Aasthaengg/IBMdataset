S = dict()
S["a"] = input()
S["b"] = input()
S["c"] = input()

turn = 'a'

while True:
    if len(S[turn]) == 0:
        break
    next_turn = S[turn][0]
    S[turn] = S[turn][1:]
    turn = next_turn

print(turn.upper())
