S = input()
if not S[0] == 'A':
    print('WA')
    exit()
if not S[2:-1].count('C') == 1:
    print('WA')
    exit()
if not (S[1] + S[2:-1].replace('C', '') + S[-1]).islower():
    print('WA')
    exit()
print('AC')
