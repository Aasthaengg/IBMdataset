w, h, n = [int(s) for s in input().split()]
temp_list = [[True] * w for _ in range(h)]
for _ in range(n):
    xs, xe, ys, ye = 0, w, 0, h
    x, y, a = [int(s) for s in input().split()]
    if a == 1:
        xe = x
    elif a == 2:
        xs = x
    elif a == 3:
        ye = y
    elif a == 4:
        ys = y
    for i in range(ys, ye):
        for j in range(xs, xe):
            temp_list[i][j] = False
ans = 0
for i in range(h):
    for j in range(w):
        if temp_list[i][j]:
            ans += 1
print(ans)