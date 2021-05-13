n,m=map(int,input().split())
x=[0 for i in range(n)]
a=[0 for j in range(m)]
ans=0
for i in range(n):
    x[i]=list(map(int,input().split()))
    for j in range(1,x[i][0]+1):
         a[x[i][j]-1]+=1

for s in range(m):
    if n==a[s]:
        ans+=1
print(ans)