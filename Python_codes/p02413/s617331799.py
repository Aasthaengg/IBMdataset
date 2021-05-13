r, c = map(int, input().split())
a = []
for _ in range(r):
    a.append(list(map(int, input().split())))
for row in a:
    row.append(sum(row))
s = []
for column in range(c + 1):
    tmp = 0
    for row in range(r):
        tmp += a[row][column]
    s.append(tmp)
a.append(s)
for row in a:
    count = 0
    for i in row:
        if count != c:
            print('{} '.format(i), end = '')
        else:
            print('{}'.format(i), end = '')
        count += 1
    print('')

