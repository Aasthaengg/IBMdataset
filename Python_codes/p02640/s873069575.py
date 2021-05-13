x, y = map(int, input().split())
if y % 2 == 1:
    print('No')
else:
    for i in range(x + 1):
        foot = i * 2 + (x - i) * 4
        if foot == y:
            print('Yes')
            exit()
    print('No')