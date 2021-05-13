a, b, x = map(int, input().split())

t = x - a

if a > x:
    print('NO')
    exit()

if b >= t:
    print('YES')
else:
    print('NO')