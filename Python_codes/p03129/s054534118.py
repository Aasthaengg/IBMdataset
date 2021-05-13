n, k = map(int, input().split())
if n%2 == 0:
    if n//2 >= k:
        print('YES')
    else:
        print('NO')
else:
    if n//2+1 >= k:
        print('YES')
    else:
        print('NO')
