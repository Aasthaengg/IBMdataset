S = input()
if len(S) == 1:
    print('YES')
    exit()
if len(set(list(S))) == 1 or (len(set(list(S))) == 2 and len(S) != 2):
    print('NO')
    exit()
cnt = [S.count('a'),S.count('b'),S.count('c')]
if max(cnt)-min(cnt) <= 1:
    print('YES')
else:
    print('NO')