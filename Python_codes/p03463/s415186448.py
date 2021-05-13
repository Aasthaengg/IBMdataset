n, a, b = map(int, input().split())

if n == b and abs(a - b) == 1:
    print('Borys')
elif abs(a - b) % 2 == 0:
    print('Alice')
elif abs(a - b) % 2 != 0:
    print('Borys')
else:
    print('Draw')