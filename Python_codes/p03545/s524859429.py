from itertools import product
S = input()
n = len(S)
bit = list(product([0, 1], repeat = n - 1))
for state in bit:
    ans = int(S[0])
    s = S[0]
    for i in range(len(state)):
        if state[i] == 1:
            s += '+' + S[i + 1]
            ans += int(S[i + 1])
        else:
            s += '-' + S[i + 1]
            ans -= int(S[i + 1])
    if ans == 7:
        print(s + '=7')
        break
