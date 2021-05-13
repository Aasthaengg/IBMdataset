a,b,x = list(map(int,input().split()))

if a > x:
    print('NO')
else:
    if a+b >= x:
        print('YES')
    else:
        print('NO')
