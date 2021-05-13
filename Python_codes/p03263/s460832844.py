H,W = map(int,input().split())
a = [list(map(int,input().split())) for i in range(H)]

ans = []

for i in range(H):
    if i%2:
        for j in range(W-1,0,-1):
            if a[i][j]%2:
                a[i][j] -= 1
                a[i][j-1] += 1
                ans.append([i+1,j+1,i+1,j])
        if i != H-1 and a[i][0]%2:
            a[i][0] -= 1
            a[i+1][0] += 1
            ans.append([i+1,1,i+2,1])

    else:
        for j in range(W-1):
            if a[i][j]%2:
                a[i][j] -= 1
                a[i][j+1] += 1
                ans.append([i+1,j+1,i+1,j+2])
        if i != H-1 and a[i][W-1]%2:
            a[i][W-1] -= 1
            a[i+1][W-1] += 1
            ans.append([i+1,W,i+2,W])
print(len(ans))
for an in ans:
    print(' '.join(map(str,an)))
