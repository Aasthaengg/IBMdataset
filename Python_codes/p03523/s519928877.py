S = input().strip()

if S.find('AA') != -1:
    print('NO')
    exit()

if S.find('KAI') != -1:
    print('NO')
    exit()

if S.find('IAH') != -1:
    print('NO')
    exit()

if S.replace('A', '') == 'KIHBR':
    print('YES')
else:
    print('NO')