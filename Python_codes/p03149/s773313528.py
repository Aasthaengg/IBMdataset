N = input().split()
if all(N.count(x) == 1 for x in '1974'):
    print('YES')
else:
    print('NO')