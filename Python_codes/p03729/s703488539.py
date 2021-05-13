str = input().split()
a, b, c = str

if(a.endswith(b[0]) and b.endswith(c[0])):
    print('YES')
else:
    print('NO')