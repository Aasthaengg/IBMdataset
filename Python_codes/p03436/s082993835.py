def resolve():
    H, W = list(map(int, input().split()))
    C = [list(input()) for i in range(H)]
    passed = [[False for _ in range(W)] for _ in range(H)]
    import collections
    q = collections.deque([[0,0,1]])
    minhop = float("inf")    
    while q:
        y, x, cnt = q.popleft()
        if y == H-1 and x == W-1:
            minhop = min(minhop, cnt)
            continue
        if passed[y][x]:
            continue
        passed[y][x] = True
        for i, j in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            _y, _x = y+i, x+j
            if 0 <= _y < H and 0 <= _x < W and C[_y][_x] == ".":
                q.append([_y, _x, cnt+1])
    
    nblack = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                nblack += 1
    print(H*W-minhop-nblack if minhop != float("inf") else -1)

if '__main__' == __name__:
    resolve()