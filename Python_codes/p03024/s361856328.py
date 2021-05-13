s = list(input())

x = 15 - len(s)
y = s.count('o')

if x + y >= 8:
    print('YES')
else:
    print('NO')


