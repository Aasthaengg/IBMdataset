N = int(input())
lis = []
for _ in range(N):
    x, y, h = map(int, input().split())
    if h > 0:
        sx, sy, sh = x, y, h
    lis.append((x, y, h))
for i in range(101):
    for j in range(101):
        high = sh + abs(sx - i) + abs(sy - j)
        judge = -1
        for x, y, h in lis:
            if h > 0 and high != h + abs(x - i) + abs(y - j):
                judge = 0
                break
        if judge == 0:
            continue
        for x, y, h in lis:
            if h == 0 and high > abs(x - i) + abs(y - j):
                judge = 0
                break
        if judge == 0:
            continue
        
        print(i, j, sh + abs(sx - i) + abs(sy - j))
        exit()