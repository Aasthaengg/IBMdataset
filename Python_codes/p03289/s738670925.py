S = input()
charset = set(list(S))
if 'A' in charset:
    charset.remove('A')
if 'C' in charset:
    charset.remove('C')
# print(f'S:{S} charset:{charset}', file=sys.stderr)
if S[0] == 'A' and S[2:-1].count('C') == 1 and ''.join(charset).islower():
    print('AC')
else:
    print('WA')