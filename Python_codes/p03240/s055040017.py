N = int(input())

Point = []
for _ in range(N):
    Point.append(tuple(map(int, input().split())))
Point.sort(key=lambda x: x[2], reverse=True)

for cx in range(101):
    for cy in range(101):
        x, y, h = Point[0]
        H = h + abs(x-cx) + abs(y-cy)
        flag = True
        for i in range(1,N):
            nx, ny, nh = Point[i]
            if max(H - abs(nx-cx) - abs(ny-cy),0) != nh:
                flag = False
                break
        if flag:
            print(cx, end=' ')
            print(cy, end=' ')
            print(H, end=' ')
            exit()