H,W = map(int,input().split())
S = [input() for _ in range(H)]
A = [[0]*W for _ in range(H)]
B = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            A[i][j] = "#"
for i in range(H):
    for j in range(W):
        if A[i][j] != "#":
            for dx,dy in B:
                if 0 <= j+dx <= W-1 and 0 <= i+dy <= H-1:
                    if A[i+dy][j+dx] == "#":
                        A[i][j] += 1
for i in A:
    print(*i, sep = "")