H,W=map(int,input().split())
S=[input()for _ in range(H)]

w1=[[]for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j]=='#':
            w1[i].append(j)
    w1[i].append(W)

w2=[[0]*W for _ in range(H)]
for i in range(H):
    k=0
    L=-1
    R=w1[i][k]
    for j in range(W):
        if S[i][j]=='#':
            L=w1[i][k]
            k+=1
            R=w1[i][k]
            continue
        w2[i][j]=R-L-1

h1=[[]for _ in range(W)]
for j in range(W):
    for i in range(H):
        if S[i][j]=='#':
            h1[j].append(i)
    h1[j].append(H)

h2=[[0]*W for _ in range(H)]
for j in range(W):
    k=0
    L=-1
    R=h1[j][k]
    for i in range(H):
        if S[i][j]=='#':
            L=h1[j][k]
            k+=1
            R=h1[j][k]
            continue
        h2[i][j]=R-L-1

print(max(w2[i][j]+h2[i][j]-1 for i in range(H)for j in range(W)))