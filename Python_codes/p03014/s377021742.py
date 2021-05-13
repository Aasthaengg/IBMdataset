H, W = map(int,input().split())
S = []
for _ in range(H):
    S.append(input())


yoko, tate = [], []
for h in range(H):
    now = []
    
    w, cnt = 0, 0
    while True:
        if not w < W:
            for _ in range(cnt): now.append(cnt) 
            break

        if S[h][w] == "#":
            for _ in range(cnt): now.append(cnt)
            now.append(0)
            cnt = 0
        else:
            cnt += 1

        w += 1

    yoko.append(now)

for w in range(W):
    now = []
    
    h, cnt = 0, 0
    while True:
        if not h < H:
            for _ in range(cnt): now.append(cnt) 
            break

        if S[h][w] == "#":
            for _ in range(cnt): now.append(cnt)
            now.append(0)
            cnt = 0
        else:
            cnt += 1

        h += 1
    
    tate.append(now)

ans = 0
for h in range(H):
    for w in range(W):
        ans = max(ans, yoko[h][w]+tate[w][h]-1)
    
print(ans)