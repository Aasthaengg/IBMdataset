H, W = list(map(int, input().split()))
d = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j, x in enumerate(list(input())):        
        if x == "#":
            s = 0
        else:
            s = 1
        d[i][j] = s

# 自分より左のOKマスの数
L = [[0 for _ in range(W)] for _ in range(H)]
# 自分より右のOKマスの数
R = [[0 for _ in range(W)] for _ in range(H)]
# 自分より上のOKマスの数
U = [[0 for _ in range(W)] for _ in range(H)]
# 自分より下のOKマスの数
D = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        # for L
        if d[i][j]:
            if j == 0:
                L[i][j] = 1            
            else:
                L[i][j] = L[i][j-1] + 1
        else:
            L[i][j] = 0
        
        # for R
        rj = W - j - 1
        if d[i][rj]:
            if rj == W-1:
                R[i][rj] = 1            
            else:
                R[i][rj] = R[i][rj+1] + 1
        else:
            R[i][rj] = 0
        
        # for U        
        if d[i][j]:
            if i == 0:
                U[i][j] = 1            
            else:
                U[i][j] = U[i-1][j] + 1
        else:
            U[i][j] = 0
     
        # for D
        di = H - i - 1
        if d[di][j]:
            if di == H-1:
                D[di][j] = 1            
            else:
                D[di][j] = D[di+1][j] + 1
        else:
            D[di][j] = 0

m = 0
for i in range(H):
    for j in range(W):
        m = max(m, L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3)
print(m)