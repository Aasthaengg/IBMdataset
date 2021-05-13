H,W = map(int,input().split())
A = [[-1 for _ in range(W+2)]]
for _ in range(H):
    a = list(map(int,input().split()))
    a.insert(0,-1)
    a.append(-1)
    A.append(a)
for i in range(1,H+1):
    for j in range(1,W+1):
        A[i][j] = A[i][j]%2
row = 1
col = 1
cnt = 0
Op = []
while row<=H and col<=W:
    if row%2==1:
        if col<W and A[row][col]==0:
            col += 1
        elif col<W and A[row][col]==1:
            Op.append([row,col,row,col+1])
            cnt += 1
            A[row][col] = 0
            A[row][col+1] = (A[row][col+1]+1)%2
            col += 1
        elif col==W and A[row][col]==0:
            row += 1
        elif col==W and A[row][col]==1:
            if row<H:
                Op.append([row,col,row+1,col])
                cnt += 1
                A[row][col]=0
                A[row+1][col]=(A[row+1][col]+1)%2
            row += 1
    else:
        if col>1 and A[row][col]==0:
            col -= 1
        elif col>1 and A[row][col]==1:
            Op.append([row,col,row,col-1])
            cnt += 1
            A[row][col]=0
            A[row][col-1]=(A[row][col-1]+1)%2
            col -= 1
        elif col==1 and A[row][col]==0:
            row += 1
        elif col==1 and A[row][col]==1:
            if row<H:
                Op.append([row,col,row+1,col])
                cnt += 1
                A[row][col]=0
                A[row+1][col]=(A[row+1][col]+1)%2
            row += 1
print(cnt)
for i in range(cnt):
    print(*Op[i])