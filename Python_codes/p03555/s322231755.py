c1 = input()
c2 = input()
c3 = c1[::-1]
c4 = c2[::-1]
if c1 == c4 and c2 == c3:
    print('YES')
else:
    print('NO')
