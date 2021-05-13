a, b, x = map(int, input().split())
cat_min, cat_max = a, a+b
if x >= cat_min and x <= cat_max:
    print('YES')
else:
    print('NO')