H, W=map(int, input().split())
h, w=map(int, input().split())

t=[[0]*W for i in [0]*H]

for i in range(h):
    for j in range(W):
        t[i][j]=1

for i in range(w):
    for j in range(H):
        t[j][i]=1

ans=0

for i in range(H):
    for j in range(W):
        if t[i][j]==0:
            ans+=1

print(ans)