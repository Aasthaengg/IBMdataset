c = [input().split() for i in range(3)]
c = sum(c, [])
for i in '1234':
    if c.count(i) > 2:
        print('NO')
        break
else:
    print('YES')