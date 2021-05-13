h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]
L = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if j == 0 and S[i][j] != '#':
            L[i][j] = 1
        elif S[i][j] != '#':
            L[i][j] = L[i][j-1] + 1
R = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w-1, -1, -1):
        if j == w-1 and S[i][j] != '#':
            R[i][j] = 1
        elif S[i][j] != '#':
            R[i][j] = R[i][j+1] + 1
U = [[0]*w for _ in range(h)]
for j in range(w):
    for i in range(h):
        if i == 0 and S[i][j] != '#':
            U[i][j] = 1
        elif S[i][j] != '#':
            U[i][j] = U[i-1][j] + 1
D = [[0]*w for _ in range(h)]
for j in range(w):
    for i in range(h-1, -1, -1):
        if i == h-1 and S[i][j] != '#':
            D[i][j] = 1
        elif S[i][j] != '#':
            D[i][j] = D[i+1][j] + 1
ans = -1
for i in range(h):
    for j in range(w):
        ans = max(ans, L[i][j]+R[i][j]+U[i][j]+D[i][j]-3)
print(ans)