n, k = map(int, input().split())

if n % 2 != 0:
    n += 1

if n // k >= 2:
    print('YES')
else:
    print('NO')