a, b = [int(x) for x in input().split()]
if (a + b) % 3 == 0 or a % 3 == 0 or b % 3 == 0:
    print('Possible ')
else:
    print('Impossible')
