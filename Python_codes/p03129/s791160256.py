n, k = map(int, input().split())
a = [0]*n

if len(a[::2]) >= k:
    print('YES')
else:
    print('NO')
