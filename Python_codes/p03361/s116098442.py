H,W=map(int,input().split())
s=[list(input())for i in range(H)]
c=[['.']*W for i in range(H)]
for i in range(H):
    countX=0
    nowX=s[i][0]
    for j in range(W):
        if nowX==s[i][j]:
            countX+=1
            if 1<countX and nowX=='#':
                c[i][j-1],c[i][j]='#','#'
        else:
            countX=1
        nowX=s[i][j]
for i in range(W):
    countY=0
    nowY=s[0][i]
    for j in range(H):
        if nowY==s[j][i]:
            countY+=1
            if 1<countY and nowY =='#':
                c[j-1][i],c[j][i]='#','#'
        else:
            countY=1
        nowY=s[j][i]
print('Yes' if c==s else 'No')