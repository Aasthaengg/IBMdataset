H,W,K = map(int,input().split())
cake = [list(input()) for _ in range(H)]
cnt = 1

ans = [[0]*W for _ in range(H)]

for h in range(H):
    for w in range(W):
        if cake[h][w] == "#":
            ans[h][w] = cnt
            cnt += 1

for h in range(H):
    for w in range(1,W):
        if ans[h][w] == 0:
            ans[h][w] = ans[h][w-1]

for h in range(H):
    for w in range(W-2,-1,-1):
        if ans[h][w] == 0:
            ans[h][w] = ans[h][w+1]

for h in range(1,H):
    for w in range(W):
        if ans[h][w] == 0:
            ans[h][w] = ans[h-1][w]

for h in range(H-2,-1,-1):
    for w in range(W):
        if ans[h][w] == 0:
            ans[h][w] = ans[h+1][w]

for h in range(H):
    print(*ans[h])
