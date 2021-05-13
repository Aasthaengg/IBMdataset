N = int(input())

for i in range(N):
    sides = sorted(list(map(int, input().split())))
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print('YES')
    else:
        print('NO')

