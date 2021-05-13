n=int(input())
d=[]

for i in range(n):
    tmp=[int(j) for j in input().split()]
    d.append(tmp)

ans=[[0]*n for i in range(n)]

for i in range(n):
    for j in range(i+1,n):
        ans[i][j]=d[i][j]

for i in range(n):
    for j in range(i+1,n):
        for k in range(n):
            if i==k or j==k:
                continue
            if d[i][j]>d[i][k]+d[k][j]:
                print(-1)
                exit()
            elif d[i][j]==d[i][k]+d[k][j]:
                ans[i][j]=0
res=0
for i in range(n):
    res+=sum(ans[i])
print(res)
