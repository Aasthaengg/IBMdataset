n = int(input())
tp, xp, yp = 0, 0, 0
for _ in range(n):
    t, x, y = map(int, input().split())
    td = t - tp
    xd = x - xp
    yd = y - yp
    if td < abs(xd) + abs(yd) or (td - abs(xd) - abs(yd)) % 2 == 1:
        print('No')
        break
    tp = t
    xp = x
    yp = y
else:
    print('Yes')
