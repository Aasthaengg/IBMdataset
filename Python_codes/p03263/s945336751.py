H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
for i in range(H):
    for j in range(W):
        A[i][j] = A[i][j]%2
flag=0
for i in range(H):
    if i%2==0:
        for j in range(W):
            if A[i][j]==1:
                cur = (i,j)
                flag=1
                break
        if flag==1:break
    else:
        for j in range(W-1,-1,-1):
            if A[i][j]==1:
                cur = (i,j)
                flag = 1
                break
        if flag==1:break
B = []
if flag==0:
    N=0
else:
    i,j = cur
    ind = 1
    while i<H:
        if i%2==0:
            while j<W:
                if j==W-1:
                    if ind==1 and i<H-1:
                        B.append([(i,j),(i+1,j)])
                    i += 1
                    if i<H and A[i][j]==1:
                        ind = 1-ind
                    break
                else:
                    if ind==1:
                        B.append([(i,j),(i,j+1)])
                    j += 1
                    if A[i][j]==1:
                        ind = 1-ind
        else:
            while j>=0:
                if j==0:
                    if ind==1 and i<H-1:
                        B.append([(i,j),(i+1,j)])
                    i += 1
                    if i<H and A[i][j]==1:
                        ind = 1-ind
                    break
                else:
                    if ind==1:
                        B.append([(i,j),(i,j-1)])
                    j -= 1
                    if A[i][j]==1:
                        ind = 1-ind
    N = len(B)
print(N)
for i in range(N):
    (i1,j1),(i2,j2)=B[i]
    print(i1+1,j1+1,i2+1,j2+1)