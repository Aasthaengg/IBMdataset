n = int(input())
for i in range(n):
    a = sorted([int(x) for x in input().split()])
    if a[0] ** 2 + a[1] ** 2 == a[2] ** 2:
        print('YES')
    else:
        print('NO')