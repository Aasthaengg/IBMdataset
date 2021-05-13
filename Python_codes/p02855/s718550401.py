H,W,K = list(map(int,input().split()))
S = []
for i in range(H):
    S.append(list(input()))

rowcnt = [0]*H
ULrow = H
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            rowcnt[i]+=1
            ULrow = min(ULrow,i)

out = [[0]*W for i in range(H)]
now = 1
for i in range(H):
    X = rowcnt[i]
    if X!=0:
        for j in range(W):
            out[i][j]=now
            if S[i][j]=="#":
                now+=1
                X+=-1
            elif X==0:
                out[i][j] += -1

for i in range(H):
    if rowcnt[i]==0 and i<ULrow:
        for j in range(W):
            out[i][j]=out[ULrow][j]
    elif rowcnt[i]==0 and i>ULrow:
        for j in range(W):
            out[i][j]=out[i-1][j]

for i in range(H):
    print(*out[i])