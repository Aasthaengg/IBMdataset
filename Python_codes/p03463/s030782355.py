n, a, b = list(map(int, input().split(' ')))

if (b - a + 1) % 2 == 1:
    print('Alice')
else:
    print('Borys')
