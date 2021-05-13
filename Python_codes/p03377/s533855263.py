a, b, x = map(int, input().split())
if x - a > 0:
    if a + b >= x:
        print('YES')
    else:
        print('NO')
elif x == a:
    print('YES')
else:
    print('NO') 