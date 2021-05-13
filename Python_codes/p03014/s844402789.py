H, W = map(int, input().split())
S = [input() for _ in range(H)]
yoko = [[0] * W for _ in range(H)]
tate = [[0] * W for _ in range(H)]

for h in range(H):
    d = []
    for w in range(W):
        if S[h][w] == ".":
            d.append([h, w])
            if W != w+1: continue
        for h, w in d:
            yoko[h][w] = len(d)
        d = []

for w in range(W):
    d = []
    for h in range(H):
        if S[h][w] == ".":
            d.append([h, w])
            if H != h+1: continue
        for h, w in d:
            tate[h][w] = len(d)
        d = []
        
ans = 0
for h in range(H):
    for w in range(W):
        if ans < yoko[h][w]+tate[h][w]-1:
            ans = yoko[h][w]+tate[h][w]-1
print(ans)