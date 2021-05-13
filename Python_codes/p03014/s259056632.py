H,W = map(int,input().split())
S = [input().strip() for _ in range(H)]
X = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    j = 0
    cur = j
    while j<W:
        if S[i][j]==".":
            j += 1
        else:
            for k in range(cur,j):
                X[i][k] = j-cur
            j += 1
            cur = j
    for k in range(cur,W):
        X[i][k] = W-cur
Y = [[0 for _ in range(W)] for _ in range(H)]
for j in range(W):
    i = 0
    cur = i
    while i<H:
        if S[i][j]==".":
            i += 1
        else:
            for k in range(cur,i):
                Y[k][j] = i-cur
            i += 1
            cur = i
    for k in range(cur,H):
        Y[k][j] = H-cur
cmax = 0
for i in range(H):
    for j in range(W):
        if S[i][j]==".":
            cmax = max(cmax,X[i][j]+Y[i][j]-1)
print(cmax)