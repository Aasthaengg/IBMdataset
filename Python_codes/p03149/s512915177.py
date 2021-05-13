a, b, c, d = map(int, input().split())
l = [a, b, c, d]
l.sort()
if l[0] == 1 and l[1] == 4 and l[2] == 7 and l[3] == 9:
    print('YES')
else:
    print('NO')