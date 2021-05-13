S = input()
N = len(S)

nokori = 15 - N

if S.count('o') + nokori >= 8:
    print('YES')
else:
    print('NO')
