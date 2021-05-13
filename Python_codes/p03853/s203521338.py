H,W=map(int,input().split())
C=[list(input()) for _ in range(H)]
newc=[[None]*W for _ in range(2*H)]
for i in range(2*H):
    for j in range(W):
        newc[i][j]=C[i//2][j]
for i in range(2*H):
    for j in range(W):
        print(newc[i][j],end="")
    print("\n")
