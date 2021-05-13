n = int(input())
data = [sorted(map(int, input().split(' '))) for i in range(n)]

for d in data:
    if d[0]**2 + d[1]**2 == d[2]**2:
        print('YES')
    else:
        print('NO')