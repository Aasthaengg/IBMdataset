S = input()
a = S.count('a')
b = S.count('b')
c = S.count('c')

if abs(a-b) < 2 and abs(b-c) < 2 and abs(c-a) < 2:
    print('YES')
else:
    print('NO')
