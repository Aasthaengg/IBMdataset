H,W=map(int,input().split())
C=[list(map(str,input().split())) for i in range(H)]
ans=[[] for i in range(2*H)]
for i in range(H):
    ans[2*i]=C[i]
    ans[2*i+1]=C[i]

for j in range(2*H):
    print(*ans[j])