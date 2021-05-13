x = int(input())

n = x // 100
if 100 * n <= x <= 105 * n:
    print('1')
else:
    print('0')