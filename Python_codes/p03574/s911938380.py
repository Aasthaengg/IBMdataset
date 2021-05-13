H,W = map(int,input().split())
masu = [list(input()) for _ in range(H)]

def kazu(h,w):
    houkou = [[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1]]
    count = 0
    for ya in houkou:
        if 0 <= h+ya[0] < H and 0 <= w+ya[1] < W:
            if masu[h+ya[0]][w+ya[1]] == '#':
                count += 1

    return count

for w in range(W):
    for h in range(H):
        if masu[h][w]=='.':
            masu[h][w] = kazu(h,w)

for l in masu:print(*l,sep='')
