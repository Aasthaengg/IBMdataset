N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
for i in lst:
    i.sort()
    if i[0] ** 2 + i[1] ** 2 == i[2] ** 2:
        print('YES')
    else:
        print('NO')

