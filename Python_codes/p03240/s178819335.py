
N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]

ans = []
X.sort(key=lambda x: x[2])
for c_x in range(0, 101):
    for c_y in range(0, 101):
        height = X[-1][2] + abs(X[-1][0] - c_x) + abs(X[-1][1] - c_y)
        flag = True
        for x, y, h in X:
            flag &= h == max(height - abs(x - c_x) - abs(y - c_y), 0)

        if flag:
            print(c_x, c_y, height)
            exit()
