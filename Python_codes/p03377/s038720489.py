a, b, x = [int(x) for x in input().split()]

if a <= x <= a + b:
    print('YES')
else:
    print('NO')