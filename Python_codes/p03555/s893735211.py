c1 = input()
c2 = input()

rc1 = c1[::-1]
rc2 = c2[::-1]


if c2 == rc1 and c1 == rc2:
    print('YES')
else:
    print('NO')