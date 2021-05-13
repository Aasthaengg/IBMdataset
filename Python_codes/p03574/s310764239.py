H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

T = [[0]*(W+2) for _ in range(H+2)]

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            T[i+1][j+1] = 9

for i in range(1,H+1):
    for j in range(1,W+1):
        if T[i][j] >= 9:
            T[i-1][j-1] += 1
            T[i-1][j+0] += 1
            T[i-1][j+1] += 1
            T[i+0][j-1] += 1
            T[i+0][j+0] += 1
            T[i+0][j+1] += 1
            T[i+1][j-1] += 1
            T[i+1][j+0] += 1
            T[i+1][j+1] += 1

for i in range(1,H+1):
    ans = ""
    for j in range(1,W+1):
        if T[i][j] >= 9:
            T[i][j] = "#"
        ans += str(T[i][j])
    print(ans)
