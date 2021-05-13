n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
for i in info:
    if i[2] > 0:
        x, y, h = i[0], i[1], i[2]
        break
for i in range(101):
    for j in range(101):
        H = h + abs(x - i) + abs(y - j)
        if all(max(H - abs(k[0] - i) - abs(k[1] - j), 0) == k[2] for k in info):
            print(i, j, H)