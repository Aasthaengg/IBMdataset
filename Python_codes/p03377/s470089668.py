a, b, x = input().strip().split()
a = int(a)
b = int(b)
x = int(x)
c = x - a
if 0 <= c <= b:
    print('YES')
else:
    print('NO')
