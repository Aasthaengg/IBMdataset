H,W = map(int,input().split())
a = [None]*H
for i in range(H):
    a[i] = list(map(int, input().split() ) )

ans=[]
for i in range(H):
    for j in range(W):
        
        if i==H-1 and j==W-1:
            continue
        if a[i][j]%2==1:
            if j!=W-1:
                ans.append((i,j,i,j+1))
                a[i][j+1]+=1
            else:
                ans.append((i,j,i+1,j))
                a[i+1][j]+=1
print(len(ans))
for aa in ans:
    print(*[aaa+1 for aaa in aa])