import collections
H,W=map(int,input().split())
s=[list(str(input()))for i in range(H)]

ss=[['' for j  in range(W+2)]for i in range(H+2)]
for i in range(H):
    for j in range(W):
        ss[i+1][j+1]=s[i][j]

for i in range(H):
    for j in range(W):
        if ss[i][j]=='#':
            if ss[i][j-1]=='#' or ss[i][j+1]=='#' or ss[i-1][j]=='#' or ss[i+1][j]=='#':
                continue
            else:
                print('No')
                exit()
print('Yes')