S = input()
Ss = '{}s'.format(S) if not S.endswith('s') else '{}es'.format(S)
print(Ss)