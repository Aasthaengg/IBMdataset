W, H, N = map(int, input().split(' '))

area = []
area_w = []
for h in range(H):
    for w in range(W):
        area_w.append(0)
    area.append(area_w)
    area_w = []

for n in range(N):
    X,Y,a = map(int, input().split(' '))
    if a == 1:
        for h in range(H):
            for x in range(X):
                area[h][x] = 1
    elif a == 2:
        for h in range(H):
            for x in range(X,W):
                area[h][x] = 1 
    elif a == 3:
        for y in range(Y):
            for w in range(W):
                area[y][w] = 1
    else:
        for y in range(Y,H):
            for w in range(W):
                area[y][w] = 1
sum_area = 0
for h in range(H):
    sum_area += sum(area[h])

ans = H*W - sum_area
print(ans)