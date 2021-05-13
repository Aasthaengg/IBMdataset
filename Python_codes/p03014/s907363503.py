H, W = map(int, input().split())
S = [input() for _ in range(H)]

yoko = [[0]*W for _ in range(H)]
tate = [[0]*W for _ in range(H)]

def f(l):
    print("\n".join("".join(map(str, row)) for row in l))

for h in range(H):
    if S[h][0] == ".":
        yoko[h][0] = 1
    else:
        yoko[h][0] = 0

for h in range(H):
    for w in range(1, W):
        if S[h][w] == ".":
            yoko[h][w] = yoko[h][w-1]+1
        else:
            yoko[h][w] = 0

for h in range(H):
    for w in range(W-2, -1, -1):
        if S[h][w]=="." and S[h][w+1]==".":
            yoko[h][w] = yoko[h][w+1]

for w in range(W):
    if S[0][w] == ".":
        tate[0][w] = 1
    else:
        tate[0][w] = 0

for w in range(W):
    for h in range(1, H):
        if S[h][w] == ".":
            tate[h][w] = tate[h-1][w]+1
        else:
            tate[h][w] = 0

for w in range(W):
    for h in range(H-2, -1, -1):
        if S[h][w]=="." and S[h+1][w]==".":
            tate[h][w] = tate[h+1][w]

ans = 0

for h in range(H):
    for w in range(W):
        ans = max(yoko[h][w]+tate[h][w]-1, ans)

print(ans)