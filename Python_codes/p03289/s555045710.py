S = list(input())
if S[0] != 'A':
    print('WA')
    exit()
S[0] = 'a'
if S.count('C') != 1:
    print('WA')
    exit()
i = S.index('C')
if i == 1 or i == len(S)-1:
    print('WA')
    exit()
S[S.index('C')] = 'c'
if ''.join(S) == ''.join(S).lower():
    print('AC')
else:
    print('WA')