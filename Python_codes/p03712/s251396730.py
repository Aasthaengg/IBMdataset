H,W=map(int,input().split())
a=[list(map(str,input())) for i in range(H)]

ans=[['#' for i in range(W+2)]for j in range(H+2)]

for i in range(W):
    for j in range(H):
        ans[j+1][i+1]=a[j][i]
    
for j in range(H+2):
    print("".join(ans[j]))