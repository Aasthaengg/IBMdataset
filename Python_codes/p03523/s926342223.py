s = input()
if len(s) > 9:
    print('NO')
elif 'KA' in s or 'IA' in s:
    print('NO')
elif s.replace('A','') =='KIHBR' and not 'AA' in s:
    print('YES')
else:
    print('NO')