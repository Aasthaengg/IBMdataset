S = input()

if S[0] == 'A':
    S = S[1:]
    if S[1: -1].count('C') == 1:
        i = S[1: -1].index('C') + 1
        S = S[: i] + S[i + 1:]
        if S.islower():
            print('AC')
            exit()
print('WA')