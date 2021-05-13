for i in range(int(input())):
    a, b, c = sorted([int(i) for i in input().split()])
    print('YES' if a ** 2 + b ** 2 == c ** 2 else 'NO')

