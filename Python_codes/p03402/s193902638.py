A,B = map(int,input().split())#A=白(.)，B=黒(#)
K = 50
#でっかいグリッドを用意
grid = [['.' for i in range(2*K)] for j in range(2*K)]
#上半分を白，下半分を黒にする
for i in range(K,2*K):
    for j in range(2*K):
        grid[i][j]='#'
bcnt=0
wcnt=0
#白ベースの箇所に黒を，黒ベースの箇所に白を一個ずつ置いていく
for i in range(1,K,2):
    for j in range(0,2*K,2):
        if bcnt < B-1:
            grid[i][j]='#'
            bcnt += 1
for i in range(K+1,2*K,2):
    for j in range(0,2*K,2):
        if wcnt < A-1:
            grid[i][j]='.'
            wcnt +=1

print(2*K,2*K)
for i in range(2*K):
    row_grid=''.join(grid[i])
    print(row_grid)
