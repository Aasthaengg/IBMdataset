n, a, b = map(int, input().split())
dis = b - a - 1
if dis % 2 != 0:
    print('Alice')
else:
    print('Borys')