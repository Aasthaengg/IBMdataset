S = input()
x, y, z = sorted([S.count('a'), S.count('b'), S.count('c')])
if z-x >= 2:
    print('NO')
else:
    print('YES')