for i in range(int(input())):
    a = [int(i) for i in input().split(' ')]
    a.sort()
    if a[0]**2 + a[1]**2 == a[2]**2:
        print('YES')
    else:
        print('NO')