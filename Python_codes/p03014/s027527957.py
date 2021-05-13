def resolve():
    (H, W) = list(map(int, input().split(" ")))
    S = [list(input()) for i in range(H)]
    L = [[0 for _ in range(W)] for _ in range(H)]
    R = [[0 for _ in range(W)] for _ in range(H)]
    U = [[0 for _ in range(W)] for _ in range(H)]
    D = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            L[i][j] = L[i][j-1]+1 if j > 0 else 1
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1 ,-1):
            if S[i][j] == "#":
                continue
            R[i][j] = R[i][j+1]+1 if j < W-1 else 1
    for i in range(H-1, -1, -1):
        for j in range(W):
            if S[i][j] == "#":
                continue
            D[i][j] = D[i+1][j]+1 if i < H-1 else 1
    for i in range(H):
        for j in range(W-1, -1 ,-1):
            if S[i][j] == "#":
                continue
            U[i][j] = U[i-1][j]+1 if i > 0 else 1
    ans = 0
    for i in range(H):
        for j in range(W):
            ans = max(ans, L[i][j]+R[i][j]+U[i][j]+D[i][j]-3)

    print(ans)

if '__main__' == __name__:
    resolve()