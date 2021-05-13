a,b,c=(int(x) for x in input().split())
d = c - b
e = b - a
if d == e:
    print('YES')
else:
    print('NO')