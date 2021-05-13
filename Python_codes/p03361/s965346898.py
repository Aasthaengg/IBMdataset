H,W = map(int,input().split())
S = [input().strip() for _ in range(H)]
flag = 0
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            if j+1<W and S[i][j+1]=="#" or i-1>=0 and S[i-1][j]=="#" or j-1>=0 and S[i][j-1]=="#"\
            or i+1<H and S[i+1][j]=="#":
                continue
            else:
                flag = 1
                break
    if flag==1:break
if flag==0:
    print("Yes")
else:
    print("No")
