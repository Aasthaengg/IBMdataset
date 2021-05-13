S = input()
cnt = [S.count(x) for x in 'abc']
if max(cnt)-min(cnt) < 2:
    print('YES')
else:
    print('NO')