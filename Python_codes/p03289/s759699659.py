S = input()
if S[0] == 'A' and S.count('C', 2, -1) == 1 and S.replace('A', '').replace('C', '').islower():
    print('AC')
else:
    print('WA')