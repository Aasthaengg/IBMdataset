H,W,K = map(int,input().split())
S = [input().strip() for _ in range(H)]
A = [[0 for _ in range(W)] for _ in range(H)]
row = 0
cnt = 1
for i in range(H):
    B = []
    for j in range(W):
        if S[i][j]=="#":
            B.append(j)
    if len(B)==0:
        continue
    elif len(B)==1:
        for k in range(row,i+1):
            for j in range(W):
                A[k][j] = cnt
        cnt += 1
        row = i+1
    else:
        for l in range(len(B)):
            if l==0:
                for k in range(row,i+1):
                    for j in range(B[0]+1):
                        A[k][j] = cnt
                cnt += 1
            elif l<len(B)-1:
                for k in range(row,i+1):
                    for j in range(B[l-1]+1,B[l]+1):
                        A[k][j] = cnt
                cnt += 1
            else:
                for k in range(row,i+1):
                    for j in range(B[-2]+1,W):
                        A[k][j] = cnt
                cnt += 1
        row = i+1
if row != H:
    for i in range(row,H):
        for j in range(W):
            A[i][j] = A[i-1][j]
for i in range(H):
    print(*A[i])