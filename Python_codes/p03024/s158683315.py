S = input()
rem =  15 - len(S)

if S.count('o') + rem >= 8:
    print('YES')
else:
    print('NO')
