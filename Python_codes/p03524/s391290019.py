s = input()

a = s.count('a')
b = s.count('b')
c = s.count('c')

if abs(a - b) >= 2 or abs(b - c) >= 2 or abs(c - a) >= 2:
    print('NO')
else:
    print('YES')
