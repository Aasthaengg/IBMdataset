W, H, n = map(int, input().split())
l = [[True]*W]*H
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        for h in range(H):
            for w in range(x):
                l[h][w] = False
    elif a == 2:
        for h in range(H):
            for w in range(x, W):
                l[h][w] = False
    elif a == 3:
        for h in range(y):
            l[h] = [False]*W
    else:
        for h in range(y, H):
            l[h] = [False]*W

ans = 0
for i in range(H):
    for j in range(W):
        if l[i][j]:
            ans += 1
print(ans)