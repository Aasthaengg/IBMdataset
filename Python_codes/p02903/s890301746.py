H,W,A,B=map(int,input().split())

s=[[0 for _ in range(W)]for i in range(H)]

for i in range(H):
    for j in range(W):
        if j<A and i<B:
            s[i][j]=0
        elif j<A:
            s[i][j]=1
        elif i<B:
            s[i][j]=1
        else:
            s[i][j]=0
ans=[]
for i in range(H):
    tmp=""
    for j in range(W):
        tmp=tmp+str(s[i][j])
    ans.append(tmp)
for i in range(H):
    print(ans[i])