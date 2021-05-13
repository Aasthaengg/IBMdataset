from collections import Counter
s = input()
c = Counter(s)


x = abs(c['a'] - c['b'])
y = abs(c['a'] - c['c'])
z = abs(c['b'] - c['c'])

if max(x, y, z) < 2:
    print('YES')
else:
    print('NO')