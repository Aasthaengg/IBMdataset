H,W=map(int,input().split())
A=[list(input()) for _ in range(H)]

ans=[["#"]*(W+2) for _ in range(H+2)]
for i in range(1,H+1):
    for j in range(1,W+1):
        ans[i][j]=A[i-1][j-1]

for i in range(H+2):
    print("".join(ans[i]))