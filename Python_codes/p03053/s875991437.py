from collections import deque
def mbfs(S,H,W):
    dxy=[[1,0],[0,1],[-1,0],[0,-1]]
    while(len(d)!=0):
        h,w,x=d.popleft()
        for t,y in dxy:
            if(0<=h+t<=H-1 and 0<=w+y<=W-1 and S[h+t][w+y]!='#'):
                S[h+t][w+y]='#'
                d.append([h+t,w+y,x+1])
    return x
H,W=map(int,input().split())
A=[list(input()) for i in range(H)]
d=deque()
for i in range(H):
    for j in range(W):
        if(A[i][j]=='#'):
            d.append([i,j,0])
print(mbfs(A,H,W))