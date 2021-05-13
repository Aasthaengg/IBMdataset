N = int(input())

for i in range(N):
    adjacent_side_1, adjacent_side_2, hypotenuse = sorted(list(map(int, input().split())))
    if adjacent_side_1**2 + adjacent_side_2**2 == hypotenuse**2:
        print('YES')
    else:
        print('NO')

