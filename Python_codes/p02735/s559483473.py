import numpy as np
H,W=map(int,input().split(' '))
S = (np.array([list(input()) for i in range(H)])=='#')*1
flg=[[float("inf")]*W for i in range(H)]
flg[0][0]=S[0][0]

for i in range(H):
    for j in range(W):
        if i<H-1:
            if S[i][j]==0 and S[i+1][j]==1:
                flg[i+1][j] = min(flg[i][j]+1,flg[i+1][j])
            else:
                flg[i+1][j] = min(flg[i][j],flg[i+1][j])
        if j<W-1:
            if S[i][j]==0 and S[i][j+1]==1:
                flg[i][j+1] = min(flg[i][j]+1,flg[i][j+1])
            else:
                flg[i][j+1] = min(flg[i][j],flg[i][j+1])
print(flg[-1][-1])