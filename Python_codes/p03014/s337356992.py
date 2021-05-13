H, W = map(int, input().split())

S = [[] for _ in range(H)]
for i in range(H):
    S[i] = input()

L = [[0] * W for _ in range(H)]
R = [[0] * W for _ in range(H)]
U = [[0] * W for _ in range(H)]
D = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == "." and i - 1 < 0:
            D[i][j] = 1
        elif S[i][j] == "." and i - 1 >= 0:
            D[i][j] = D[i-1][j] + 1
        if S[i][j] == "." and j - 1 < 0:
            L[i][j] = 1
        elif S[i][j] == "." and j - 1 >= 0:
            L[i][j] = L[i][j-1] + 1

for i in reversed(range(H)):
    for j in reversed(range(W)):
        if S[i][j] == "." and i + 1 >= H:
            U[i][j] = 1
        elif S[i][j] == "." and i + 1 < H:
            U[i][j] = U[i+1][j] + 1
        if S[i][j] == "." and j + 1 >= W:
            R[i][j] = 1
        elif S[i][j] == "." and j + 1 < W:
            R[i][j] = R[i][j+1] + 1

ans = 0

for i in range(H):
    for j in range(W):
        ans = max(ans, L[i][j]+R[i][j]+U[i][j]+D[i][j]-3)

print(ans)