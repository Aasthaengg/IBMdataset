s = list(input())

if 5 <= len(s) <= 9:
    if s[0] != 'A':
        s.insert(0, 'A')
    if s[4] != 'A':
        s.insert(4, 'A')
    if s[6] != 'A':
        s.insert(6, 'A')
    if len(s) == 8:
        s.append('A')

    if s == ['A','K','I','H','A','B','A','R','A']:
        print('YES')
    else:
        print('NO')

else:
    print('NO')