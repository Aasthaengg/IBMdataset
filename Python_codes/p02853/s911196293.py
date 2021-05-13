x, y = map(int, input().split(' '))
if x == 1 and y == 1:
    print(300000 * 2 + 400000)
else:
    print(100000*((4-min(x, 4))+(4-min(y, 4))))
