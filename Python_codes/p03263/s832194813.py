H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
for i in range(H):
    for j in range(W):
        if A[i][j]%2==0:
            A[i][j]=0
        else:
            A[i][j]=1
cur = [1,1,1,0]
cnt = 0
B = []
while cur[0]<=H:
    i = cur[0]-1
    j = cur[1]-1
    a = A[i][j]
    d,h = cur[2],cur[3]
    if a==0:
        if d==1 and j<W-1:
            if h==1:
                B.append((i+1,j+1,i+1,j+2))
                cnt += 1
            cur = [i+1,j+2,d,h]
        elif d==1 and j==W-1:
            if h==1 and i+2<=H:
                B.append((i+1,j+1,i+2,j+1))
                cnt += 1
            cur = [i+2,j+1,1-d,h]
        elif d==0 and j>0:
            if h==1:
                B.append((i+1,j+1,i+1,j))
                cnt += 1
            cur = [i+1,j,d,h]
        elif d==0 and j==0:
            if h==1 and i+2<=H:
                B.append((i+1,j+1,i+2,j+1))
                cnt += 1
            cur = [i+2,j+1,1-d,h]
    else:
        if d==1 and j<W-1:
            if h==0:
                B.append((i+1,j+1,i+1,j+2))
                cnt += 1
            cur = [i+1,j+2,d,1-h]
        elif d==1 and j==W-1:
            if h==0 and i+2<=H:
                B.append((i+1,j+1,i+2,j+1))
                cnt += 1
            cur = [i+2,j+1,1-d,1-h]
        elif d==0 and j>0:
            if h==0:
                B.append((i+1,j+1,i+1,j))
                cnt += 1
            cur = [i+1,j,d,1-h]
        elif d==0 and j==0:
            if h==0 and i+2<=H:
                B.append((i+1,j+1,i+2,j+1))
                cnt += 1
            cur = [i+2,j+1,1-d,1-h]
print(cnt)
for i in range(cnt):
    print(*B[i])