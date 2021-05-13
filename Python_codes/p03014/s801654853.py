H,W = map(int,input().split())
S = [input() for i in range(H)]

U = [[0]*W for i in range(H)]
D = [[0]*W for i in range(H)]
R = [[0]*W for i in range(H)]
L = [[0]*W for i in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            U[i][j] = 0
        elif i == 0 and S[i][j] == '.':
            U[i][j] = 1
        else:
            U[i][j] = U[i-1][j] + 1
            
    for j in range(W):
        if S[i][j] == '#':
            L[i][j] = 0
        elif j == 0 and S[i][j] == '.':
            L[i][j] = 1
        else:
            L[i][j] = L[i][j-1] + 1
            
for i in range(H-1,-1,-1):
    for j in range(W-1,-1,-1):
        if S[i][j] == '#':
            D[i][j] = 0
        elif i == H-1 and S[i][j] == '.':
            D[i][j] = 1
        else:
            D[i][j] = D[i+1][j] + 1
            
    for j in range(W-1,-1,-1):
        if S[i][j] == '#':
            R[i][j] = 0
        elif j == W-1 and S[i][j] == '.':
            R[i][j] = 1
        else:
            R[i][j] = R[i][j+1] + 1
            
ans = 0 

for i in range(H):
    for j in range(W):
        ans = max(ans,U[i][j]+R[i][j]+D[i][j]+L[i][j]-3)        
print(ans)    