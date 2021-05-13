n,x,y=map(int,input().split())
x,y=x-1,y-1
adj=[[float("inf")]*n for i in range(n)]
adj[x][y]=adj[y][x]=1
for i in range(n):
    for j in range(n):
        adj[i][j]=min(abs(i-j),abs(i-x)+1+abs(y-j),abs(i-y)+1+abs(y-j))
ans=[0 for i in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        ans[adj[i][j]]+=1
for i in range(1,n):
    print(ans[i])