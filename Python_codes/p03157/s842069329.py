from collections import defaultdict

H,W = map(int, input().split())
S = [input() for _ in range(H)]

es = defaultdict(list)

for i in range(H):
    for j in range(W):
        if 0 <= i < H-1:
            if S[i][j] != S[i+1][j]:
                es[(i,j)].append((i+1, j))
                es[(i+1,j)].append((i, j))

        if 0 <= j < W-1:
            if S[i][j] != S[i][j+1]:
                es[(i,j)].append((i, j+1))
                es[(i,j+1)].append((i, j))

checked = [[False for _ in range(W)] for _ in range(H)]

ans = 0
for i in range(H):
    for j in range(W):
        b,w = 0,0
        if not checked[i][j]:
            checked[i][j] = True
            if S[i][j] == "#":
                b += 1
            else:
                w += 1
            q = es[(i,j)]
            while q:
                y,x = q.pop()
                if not checked[y][x]:
                    checked[y][x] = True
                    if S[y][x] == "#":
                        b += 1
                    else:
                        w += 1
                    q.extend(es[(y,x)])
            ans += b * w

print(ans)
