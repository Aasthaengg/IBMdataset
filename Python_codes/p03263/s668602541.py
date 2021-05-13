H, W = map(int, input().split())

As = []
for _ in range(H):
    a = list(map(int, input().split()))
    As.append(a)

ans = []
isFromExist = False
x = 0
y = 0
vec = 1
count = 0
while count < H*W:
    if not isFromExist:
        if As[y][x] % 2 == 1:
            from_yx = [y, x]
            isFromExist = True
    else:
        now = [y, x]
        ans.append(from_yx + now)
        if As[y][x] % 2 == 1:
            isFromExist = False
        else:
            from_yx = now

    if vec == 1 and x == W-1:
        vec = -1
        y += 1
    elif vec == -1 and x == 0:
        vec = 1
        y += 1
    else:
        x += vec * 1
    count += 1


N = len(ans)
print(N)
for i in range(N):
    for j in range(4):
        if j == 3:
            print(ans[i][j] + 1)
        else:
            print(ans[i][j] + 1, '', end='')
