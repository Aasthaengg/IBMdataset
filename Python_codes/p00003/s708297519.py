cnt = int(input())
values = []
for i in range(cnt):
    values.append([int(x) for x in input().split()])

for x, y, z in values:
    if z ** 2 == x ** 2 + y ** 2:
        print('YES')
    elif x ** 2 == y ** 2 + z ** 2:
        print('YES')
    elif y ** 2 == x ** 2 + z ** 2:
        print('YES')
    else:
        print('NO')