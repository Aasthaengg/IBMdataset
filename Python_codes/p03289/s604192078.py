S = input()

if S[0] == 'A':
    if S[2:-1].count('C') == 1:
        S = S[0:2] + S[2:-1].replace('C', 'c') + S[-1]
        if S[1:].islower():
            print('AC')
            exit()

print('WA')