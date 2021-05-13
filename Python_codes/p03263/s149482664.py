H,W=map(int,input().split())
a=[]

for h in range(H):
    a.append(list(map(int,input().split())))

ans=[]
for h in range(H):
    for w in range(W):
        if h==H-1 and w==W-1:break
        if a[h][w]%2==1:
            if w==W-1:
                ans.append([h+1,w+1,h+2,w+1])
                a[h][w]-=1
                a[h+1][w]+=1
            else:
                ans.append([h+1,w+1,h+1,w+2])
                a[h][w]-=1
                a[h][w+1]+=1
L=len(ans)
print(L)

for i in range(L):
    print(*ans[i])
