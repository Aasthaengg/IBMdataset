H,W=map(int,input().split())
C=[list(input()) for _ in range(H)]

ans=[]
for i in range(2*H):
    i//=2
    ans.append(C[i])

for i in range(2*H):
    print("".join(ans[i]))