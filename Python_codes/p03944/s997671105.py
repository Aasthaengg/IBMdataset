W, H, N = map(int, input().split())
field = [[1 for i in range(W)] for j in range(H)]
xya = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    x, y, a = xya[i]
    if a == 1:
        for w in range(x):
            for h in range(H):
                field[h][w] = 0
    elif a == 2:
        for w in range(x, W):
            for h in range(H):
                field[h][w] = 0

    elif a == 3:
        for w in range(W):
            for h in range(y):
                field[h][w] = 0

    elif a == 4:
        for w in range(W):
            for h in range(y, H):
                field[h][w] = 0
ans = 0
for i in field:
    ans += sum(i)
print(ans)
