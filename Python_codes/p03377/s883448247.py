a, b, x = map(int, input().split())

if x < a:
    print('NO')
elif x == a:
    print('YES')
elif x <= a + b:
    print('YES')
else:
    print('NO')