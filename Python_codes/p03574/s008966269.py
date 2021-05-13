H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            cnt = 0
            for i in range(max(h-1, 0), min(h+2, H)):
                for j in range(max(w-1, 0), min(w+2, W)):
                    if S[i][j] == "#":
                        cnt += 1
            S[h][w] = str(cnt)
    print("".join(S[h]))