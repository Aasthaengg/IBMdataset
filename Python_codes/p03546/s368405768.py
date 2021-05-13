H, W = map(int, input().split())
large_n = 100000000

C_mat = []
for i in range(10):
    C_mat.append(list(map(int, input().split())))

A_mat = []
for i in range(H):
    A_mat.append(list(map(int, input().split())))
    



for k in range(10):
    for i in range(10):
        for j in range(10):
            C_mat[i][j] = min(C_mat[i][j], C_mat[i][k]+ C_mat[k][j])
            
            
            
            
ans = 0
for i in range(H):
    for j in range(W):
        if A_mat[i][j] != -1:
            ans += C_mat[A_mat[i][j]][1]
            
print(ans)