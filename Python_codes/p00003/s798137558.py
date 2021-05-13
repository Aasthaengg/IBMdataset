N = int(input())
for i in range(N):
    a = [int(i) for i in input().split()]
    a.sort(reverse=True)
    if a[0]**2 == a[1]**2+a[2]**2:
        print('YES')
    else:
        print('NO')
