n=int(input())
a=[list(map(int,input().split())) for _ in [0]*n]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if a[i][j] > a[i][k] + a[k][j]:
                print(-1)
                exit()
ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(n):
            if i != k and j != k and a[i][j] == a[i][k] + a[k][j]:
                break
        else:
            ans += a[i][j]
    
print(ans)