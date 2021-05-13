s = input()

S = s.replace('A', '')

if S == 'KIHBR' and 'AA' not in s and 'KIH' in s:
    print('YES')
else:
    print('NO')
