H,W = map(int,input().split())
S = []
for i in range(H):
    S.append(list(input()))
L = [[0 for _ in range(W)] for _ in range(H)]
R = [[0 for _ in range(W)] for _ in range(H)]
D = [[0 for _ in range(W)] for _ in range(H)]
U = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        elif j == 0:
            L[i][j] += 1
        else:
            L[i][j] += L[i][j-1] + 1
for i in range(H):
    for j in range(-1,-W-1,-1):
        if S[i][j] == '#':
            continue
        elif j == -1:
            R[i][j] += 1
        else:
            R[i][j] += R[i][j+1] + 1
for i in range(W):
    for j in range(H):
        if S[j][i] == '#':
            continue
        elif j == 0:
            U[j][i] += 1
        else:
            U[j][i] += U[j-1][i] + 1
for i in range(W):
    for j in range(-1,-H-1,-1):
        if S[j][i] == '#':
            continue
        elif j == -1:
            D[j][i] += 1
        else:
            D[j][i] += D[j+1][i] + 1
ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans,U[i][j]+D[i][j]+L[i][j]+R[i][j]-3)
print(ans)